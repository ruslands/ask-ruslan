#!/usr/bin/env python3
"""Deterministic, privacy-gated retrieval for the Ask Ruslan knowledge base."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KB = SKILL_ROOT / "references" / "knowledge-base.json"
COLLECTIONS = {
    "experience": "experience",
    "project": "projects",
    "principle": "principles",
    "interview_qa": "interview_qa",
}
KINDS = tuple(COLLECTIONS)
TOKEN_RE = re.compile(r"[^\W_]+(?:[+#]+)?", re.UNICODE)


def normalize(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(TOKEN_RE.findall(normalized))


def tokens(value: str) -> set[str]:
    return {token for token in normalize(value).split() if len(token) > 1}


def text_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(text_values(item))
        return result
    if isinstance(value, dict):
        result = []
        for key, item in value.items():
            if key not in {"sources", "approved_by"}:
                result.extend(text_values(item))
        return result
    return []


def load_kb(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Knowledge base not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Knowledge-base root must be a JSON object")
    return data


def validate_kb(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required_root = {
        "schema_version",
        "owner_display_name",
        "publication_policy",
        *COLLECTIONS.values(),
    }
    missing = sorted(required_root - data.keys())
    if missing:
        errors.append(f"Missing root fields: {', '.join(missing)}")

    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")

    policy = data.get("publication_policy")
    if not isinstance(policy, dict) or policy.get("searchable_status") != "approved_public":
        errors.append("publication_policy.searchable_status must be approved_public")

    seen_ids: set[str] = set()
    required_by_kind = {
        "experience": ("summary", "responsibilities", "outcomes"),
        "project": ("problem", "ruslan_contribution", "decisions", "outcomes"),
        "principle": ("statement", "application"),
        "interview_qa": ("question", "answer", "supported_by"),
    }
    for kind, collection in COLLECTIONS.items():
        records = data.get(collection, [])
        if not isinstance(records, list):
            errors.append(f"{collection} must be an array")
            continue
        for index, record in enumerate(records):
            prefix = f"{collection}[{index}]"
            if not isinstance(record, dict):
                errors.append(f"{prefix} must be an object")
                continue
            record_id = record.get("id")
            if not isinstance(record_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record_id):
                errors.append(f"{prefix}.id must be lowercase kebab-case")
            elif record_id in seen_ids:
                errors.append(f"Duplicate record id: {record_id}")
            else:
                seen_ids.add(record_id)

            status = record.get("publication_status")
            if status not in {"draft", "approved_public", "private", "retired"}:
                errors.append(f"{prefix}.publication_status is invalid")

            for field in ("title", "tags", "keywords", "sources", *required_by_kind[kind]):
                if field not in record:
                    errors.append(f"{prefix} is missing {field}")

            for field in ("tags", "keywords", "sources"):
                if field in record and not isinstance(record[field], list):
                    errors.append(f"{prefix}.{field} must be an array")

            sources = record.get("sources", [])
            if isinstance(sources, list):
                for source_index, source in enumerate(sources):
                    if not isinstance(source, dict) or not source.get("type") or not source.get("reference"):
                        errors.append(f"{prefix}.sources[{source_index}] needs type and reference")

            if status == "approved_public":
                if not record.get("approved_on") or not record.get("approved_by"):
                    errors.append(f"{prefix} is public but lacks approved_on or approved_by")
                if not record.get("sources"):
                    errors.append(f"{prefix} is public but has no source")

    return errors


def phrase_score(query_normalized: str, values: list[str], weight: int) -> int:
    padded_query = f" {query_normalized} "
    return sum(
        weight
        for value in values
        if normalize(value) and f" {normalize(value)} " in padded_query
    )


def score_record(query: str, record: dict[str, Any]) -> tuple[int, list[str]]:
    query_normalized = normalize(query)
    query_tokens = tokens(query)
    reasons: list[str] = []

    tags = [str(value) for value in record.get("tags", [])]
    keywords = [str(value) for value in record.get("keywords", [])]
    technologies = [str(value) for value in record.get("technologies", [])]
    title_fields = [str(record.get("title", "")), str(record.get("question", ""))]
    body_fields = text_values(record)

    score = phrase_score(query_normalized, tags, 12)
    if score:
        reasons.append("tag phrase")
    keyword_score = phrase_score(query_normalized, keywords, 10)
    if keyword_score:
        reasons.append("keyword phrase")
    technology_score = phrase_score(query_normalized, technologies, 9)
    if technology_score:
        reasons.append("technology phrase")

    title_overlap = query_tokens & tokens(" ".join(title_fields))
    body_overlap = query_tokens & tokens(" ".join(body_fields))
    if title_overlap:
        reasons.append("title/question tokens: " + ", ".join(sorted(title_overlap)))
    if body_overlap - title_overlap:
        reasons.append("content tokens: " + ", ".join(sorted(body_overlap - title_overlap)))

    score += keyword_score + technology_score + (5 * len(title_overlap)) + len(body_overlap)
    return score, reasons


def public_records(data: dict[str, Any], requested_kind: str | None) -> list[tuple[str, dict[str, Any]]]:
    selected = (requested_kind,) if requested_kind else KINDS
    records: list[tuple[str, dict[str, Any]]] = []
    for kind in selected:
        for record in data.get(COLLECTIONS[kind], []):
            if isinstance(record, dict) and record.get("publication_status") == "approved_public":
                records.append((kind, record))
    return records


def search(data: dict[str, Any], query: str, kind: str | None, limit: int, min_score: int) -> dict[str, Any]:
    matches = []
    for record_kind, record in public_records(data, kind):
        score, reasons = score_record(query, record)
        if score >= min_score:
            matches.append(
                {
                    "ref": f"{record_kind}:{record['id']}",
                    "kind": record_kind,
                    "score": score,
                    "match_reasons": reasons,
                    "record": record,
                }
            )

    matches.sort(key=lambda item: (-item["score"], item["ref"]))
    return {
        "query": query,
        "retrieval": "deterministic_keyword_v1",
        "public_records_considered": len(public_records(data, kind)),
        "match_count": min(len(matches), limit),
        "matches": matches[:limit],
        "grounding_notice": (
            "Use only returned records for claims about Ruslan. "
            "General technical reasoning must be labeled separately."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", help="Question or search phrase")
    parser.add_argument("--kind", choices=KINDS, help="Restrict search to one collection")
    parser.add_argument("--limit", type=int, default=5, help="Maximum matches (default: 5)")
    parser.add_argument("--min-score", type=int, default=2, help="Minimum deterministic score")
    parser.add_argument("--kb", type=Path, default=DEFAULT_KB, help="Knowledge-base JSON path")
    parser.add_argument("--validate-only", action="store_true", help="Validate structure without searching")
    args = parser.parse_args()
    if not args.validate_only and not args.query:
        parser.error("--query is required unless --validate-only is used")
    if args.limit < 1 or args.min_score < 0:
        parser.error("--limit must be positive and --min-score cannot be negative")
    return args


def main() -> int:
    args = parse_args()
    try:
        data = load_kb(args.kb)
    except ValueError as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 2

    errors = validate_kb(data)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 2

    if args.validate_only:
        record_count = sum(len(data.get(collection, [])) for collection in COLLECTIONS.values())
        print(json.dumps({"valid": True, "record_count": record_count}, ensure_ascii=False, indent=2))
        return 0

    print(
        json.dumps(
            search(data, args.query, args.kind, args.limit, args.min_score),
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
