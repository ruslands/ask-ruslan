#!/usr/bin/env python3
"""Import Ask Ruslan Markdown sources into reviewable knowledge-base drafts.

The importer is intentionally conservative:

* generated records always start as ``draft``;
* duplicate interview questions are collapsed, keeping the first occurrence;
* existing public, private, or retired records are never overwritten;
* unrelated hand-authored records are preserved.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parent.parent
REFERENCES = SKILL_ROOT / "references"
DEFAULT_KB = REFERENCES / "knowledge-base.json"
INTRO_PATH = REFERENCES / "my-intro.md"
QUESTIONS_PATH = REFERENCES / "typical-questions.md"
COLLECTIONS = ("experience", "projects", "principles", "interview_qa")


def source(reference: str) -> list[dict[str, str]]:
    return [{"type": "ruslan_statement", "reference": reference}]


def core_records() -> dict[str, list[dict[str, Any]]]:
    """Return narrow, curated facts represented in my-intro and interview sources."""
    return {
        "experience": [
            {
                "id": "backend-architecture-career",
                "publication_status": "draft",
                "title": "Backend development and system architecture career",
                "tags": ["backend", "architecture", "career"],
                "keywords": [
                    "backend development",
                    "system architecture",
                    "more than ten years",
                    "бэкенд-разработка",
                    "архитектура систем",
                    "больше десяти лет",
                ],
                "sources": source("references/my-intro.md#L1"),
                "summary": (
                    "Ruslan has more than ten years of experience in backend development "
                    "and system architecture. He began in data science at Sberbank Life "
                    "Insurance and later worked as a developer or architect, including for "
                    "European companies."
                ),
                "responsibilities": [
                    "Backend development",
                    "System architecture",
                    "Turning existing technologies into working products",
                ],
                "outcomes": [],
            },
            {
                "id": "ml-data-science-background",
                "publication_status": "draft",
                "title": "Machine-learning and data-science background",
                "tags": ["machine-learning", "data-science", "career"],
                "keywords": [
                    "ML experience",
                    "NLP experience",
                    "classical models",
                    "actuarial data",
                    "insurance data",
                    "опыт ML",
                ],
                "technologies": ["Python", "LSTM"],
                "sources": source("references/typical-questions.md#question-1"),
                "period": "2014–2018",
                "summary": (
                    "Ruslan describes about four and a half years in a dedicated ML role, "
                    "applying classical models to actuarial and insurance data before "
                    "focusing on backend engineering and system architecture."
                ),
                "responsibilities": [
                    "Applied classical machine-learning models to actuarial and insurance data"
                ],
                "outcomes": [],
            },
        ],
        "projects": [
            {
                "id": "samokat-backend-driven-ui",
                "publication_status": "draft",
                "title": "Samokat Backend-Driven UI platform",
                "tags": ["architecture", "backend", "mobile"],
                "keywords": [
                    "Samokat",
                    "Самокат",
                    "Backend-Driven UI",
                    "BDUI",
                    "ADR",
                    "mobile applications",
                ],
                "sources": source("references/my-intro.md#L3"),
                "problem": (
                    "Enable changes to the content and behavior of native mobile interfaces "
                    "without requiring a new app-store release."
                ),
                "ruslan_contribution": [
                    "Joined near the start of the project as the second person after the manager and was responsible for architecture",
                    "Defined the system structure",
                    "Prepared architecture documentation, ADRs, and diagrams",
                    "Presented and defended decisions to platform architects",
                ],
                "decisions": [
                    "Defined service boundaries and API contracts for the Backend-Driven UI platform"
                ],
                "outcomes": [],
            },
            {
                "id": "sber-ai-agent-anomaly-monitoring",
                "publication_status": "draft",
                "title": "Sber AI-agent anomaly-monitoring service",
                "tags": ["ai-agents", "mlops", "monitoring"],
                "keywords": [
                    "Sber",
                    "Сбер",
                    "AI-agent monitoring",
                    "anomaly detection",
                    "MLOps",
                    "LSTM",
                ],
                "technologies": ["LSTM"],
                "sources": source("references/my-intro.md#L5"),
                "problem": (
                    "Create an anomaly-monitoring service for AI agents developed by different product teams."
                ),
                "ruslan_contribution": [
                    "Joined a new two-person team as a developer and MLOps engineer",
                    "Defined the service boundaries and logic",
                    "Selected and implemented a scientific approach to detecting deviations",
                ],
                "decisions": [
                    "Selected the anomaly-detection approach used by the service"
                ],
                "outcomes": ["The team launched the product in production in four months"],
            },
            {
                "id": "echo-dictation",
                "publication_status": "draft",
                "title": "Echo Dictation",
                "tags": ["ai-product", "speech", "product-development"],
                "keywords": [
                    "Echo Dictation",
                    "dictation",
                    "meeting transcription",
                    "voice transcription",
                ],
                "sources": source("references/my-intro.md#L7"),
                "problem": "Provide dictation and meeting transcription in an application.",
                "ruslan_contribution": ["Built the Echo Dictation application"],
                "decisions": [],
                "outcomes": [],
            },
            {
                "id": "aiva-agent-platform",
                "publication_status": "draft",
                "title": "Aiva voice and chat agent platform",
                "tags": ["ai-agents", "backend", "architecture", "product-development"],
                "keywords": [
                    "Aiva",
                    "voice agents",
                    "chat agents",
                    "голосовые агенты",
                    "чат-агенты",
                    "telephony",
                    "RAG",
                    "CRM integrations",
                ],
                "technologies": [
                    "Python",
                    "FastAPI",
                    "PostgreSQL",
                    "pgvector",
                    "Redis",
                    "Gemini",
                    "OpenAI Realtime",
                    "xAI",
                    "LangChain",
                    "Langfuse",
                    "SIP",
                ],
                "sources": [
                    {
                        "type": "ruslan_statement",
                        "reference": "references/my-intro.md#L7",
                    },
                    {
                        "type": "ruslan_statement",
                        "reference": "references/typical-questions.md",
                    },
                ],
                "problem": (
                    "Build a multi-user platform for business voice and chat agents, including "
                    "telephony, knowledge retrieval, integrations, deployment, and monitoring."
                ),
                "ruslan_contribution": [
                    "Owns product and development together with a small team",
                    "Built the platform's technical core and backend",
                    "Designed agent execution, telephony, model-provider adapters, RAG, and business integrations",
                    "Implemented deployment, monitoring, and production diagnostics",
                ],
                "decisions": [
                    "Selected reusable open-source components",
                    "Separated real-time model providers behind adapters",
                    "Designed team, user, role, and access-control boundaries",
                ],
                "outcomes": [
                    "Built a multi-user platform with separate teams, users, roles, and permissions",
                    "Supported inbound enquiries, lead qualification, customer support, and outbound campaigns",
                ],
            },
        ],
        "principles": [
            {
                "id": "spec-driven-ai-development",
                "publication_status": "draft",
                "title": "Spec-driven development with AI agents",
                "tags": ["ai-assisted-development", "engineering-process", "architecture"],
                "keywords": [
                    "spec-driven development",
                    "AI coding agents",
                    "Codex",
                    "Spec Kit",
                    "ER diagrams",
                    "UML",
                    "BPMN",
                    "Mermaid",
                ],
                "technologies": ["Codex", "Spec Kit", "Mermaid", "UML", "BPMN"],
                "sources": source("references/my-intro.md#L9"),
                "statement": (
                    "Use a spec-driven workflow in which AI agents help turn dictated context "
                    "into requirements, questions, plans, and tasks, while the engineer reviews "
                    "the artifacts and makes the decisions."
                ),
                "application": (
                    "Ruslan provides agents with both text and diagrams, including ER, UML, and "
                    "BPMN diagrams generated with Mermaid, to make system relationships and "
                    "design problems easier to inspect."
                ),
                "exceptions": [],
            }
        ],
        "interview_qa": [],
    }


TECHNOLOGIES = {
    "python": "Python",
    "fastapi": "FastAPI",
    "asyncio": "asyncio",
    "sqlalchemy": "SQLAlchemy",
    "postgresql": "PostgreSQL",
    "pgvector": "pgvector",
    "redis": "Redis",
    "gemini": "Gemini",
    "openai realtime": "OpenAI Realtime",
    "xai": "xAI",
    "grok voice": "Grok Voice",
    "langchain": "LangChain",
    "langfuse": "Langfuse",
    "yandex ai studio": "Yandex AI Studio",
    "vllm": "vLLM",
    "prometheus": "Prometheus",
    "grafana": "Grafana",
    "loki": "Loki",
    "promtail": "Promtail",
    "sentry": "Sentry",
    "terraform": "Terraform",
    "cloud-init": "cloud-init",
    "bitrix24": "Bitrix24",
    "amocrm": "amoCRM",
    "telegram": "Telegram",
    "whatsapp": "WhatsApp",
    "s3": "S3",
    "sip": "SIP",
    "lstm": "LSTM",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "nuxt": "Nuxt",
    "vue": "Vue",
    "react": "React",
    "vite": "Vite",
    "node.js": "Node.js",
    "mcp": "MCP",
    "a2a": "A2A",
    "rag": "RAG",
}


TOPIC_RULES = (
    ("machine-learning", ("machine learning", " ml ", "nlp", "lstm", "fine-tun")),
    ("llm", ("llm", "language model", "модел")),
    ("ai-agents", ("agent", "агент")),
    ("rag", ("rag", "embedding", "vector", "базе знаний", "базы знаний")),
    ("backend", ("backend", "бэкенд", "fastapi", "python")),
    ("architecture", ("architect", "архитектур", "service boundaries", "границ")),
    ("leadership", ("leadership", "лидер", "руковод", "координиров")),
    ("mentoring", ("mentor", "настав")),
    ("observability", ("monitor", "метрик", "tracing", "лог", "incident", "инцидент")),
    ("reliability", ("reliab", "надеж", "race", "гонк", "timeout", "повторн")),
    ("integrations", ("integrat", "интеграц", "crm", "webhook")),
    ("devops", ("devops", "terraform", "deployment", "развертыван")),
    ("multi-agent", ("multi-agent", "multiagent", "мультиагент")),
    ("marketing", ("marketing", "маркетинг", "campaign", "кампан")),
)


def normalize_question(value: str) -> str:
    value = re.sub(r"[*_`]+", "", value)
    return " ".join(value.casefold().split())


def parse_interview_questions() -> tuple[list[dict[str, Any]], list[int]]:
    text = QUESTIONS_PATH.read_text(encoding="utf-8")
    parts = re.split(r"^##\s+(\d+)\.\s+Вопрос\s*$", text, flags=re.MULTILINE)
    records: list[dict[str, Any]] = []
    duplicate_numbers: list[int] = []
    seen_questions: set[str] = set()

    for index in range(1, len(parts), 2):
        number = int(parts[index])
        body = parts[index + 1]
        question_and_answer = re.split(
            r"^\*\*Ответ:\*\*\s*$", body, maxsplit=1, flags=re.MULTILINE
        )
        if len(question_and_answer) != 2:
            raise ValueError(f"Question {number} has no **Ответ:** separator")
        question = "\n\n".join(
            paragraph.strip()
            for paragraph in question_and_answer[0].strip().split("\n\n")
            if paragraph.strip()
        )
        answer = question_and_answer[1].strip()
        normalized = normalize_question(question)
        if normalized in seen_questions:
            duplicate_numbers.append(number)
            continue
        seen_questions.add(normalized)

        combined = f" {question} {answer} ".casefold()
        tags = [
            tag
            for tag, needles in TOPIC_RULES
            if any(needle in combined for needle in needles)
        ]
        if not tags:
            tags = ["career"]
        technologies = [
            display for needle, display in TECHNOLOGIES.items() if needle in combined
        ]
        keywords = list(dict.fromkeys([*tags, *technologies, "interview answer"]))

        supported_by: list[str] = []
        support_rules = (
            ("project:aiva-agent-platform", ("aiva",)),
            ("project:samokat-backend-driven-ui", ("samokat", "самокат")),
            (
                "project:sber-ai-agent-anomaly-monitoring",
                ("anomaly", "аномал", "agent-monitoring", "мониторинга аномалий"),
            ),
            ("project:echo-dictation", ("echo dictation",)),
            (
                "experience:backend-architecture-career",
                ("10 years", "10 лет", "backend experience", "опыт работы с python"),
            ),
            (
                "experience:ml-data-science-background",
                ("2014", "actuarial", "классическ", "data scientist"),
            ),
            ("principle:spec-driven-ai-development", ("spec-driven", "spec kit", "speckit")),
        )
        for reference, needles in support_rules:
            if any(needle in combined for needle in needles):
                supported_by.append(reference)

        title = " ".join(re.sub(r"[*_`]+", "", question).split())
        records.append(
            {
                "id": f"interview-{number:02d}",
                "publication_status": "draft",
                "title": title,
                "tags": tags,
                "keywords": keywords,
                "technologies": technologies,
                "sources": source(
                    f"references/typical-questions.md#question-{number}"
                ),
                "question": question,
                "answer": answer,
                "supported_by": supported_by,
            }
        )

    return records, duplicate_numbers


def intro_interview_records() -> list[dict[str, Any]]:
    paragraphs = [
        value.strip()
        for value in INTRO_PATH.read_text(encoding="utf-8").split("\n\n")
        if value.strip()
    ]
    if len(paragraphs) != 6:
        raise ValueError(f"Expected 6 paragraphs in my-intro.md, found {len(paragraphs)}")
    return [
        {
            "id": "interview-career-transition-2025",
            "publication_status": "draft",
            "title": "Career transition after the Samokat project",
            "tags": ["career", "ai-product"],
            "keywords": [
                "leaving Samokat",
                "career transition",
                "почему ушел из Самоката",
                "переход в AI",
            ],
            "sources": source("references/my-intro.md#L3"),
            "question": "Почему вы ушли из Самоката и чем занимались после этого?",
            "answer": paragraphs[1],
            "supported_by": ["project:samokat-backend-driven-ui"],
        },
        {
            "id": "interview-current-job-search",
            "publication_status": "draft",
            "title": "Current job-search motivation",
            "tags": ["career", "motivation", "ai-product"],
            "keywords": [
                "why looking for a job",
                "career motivation",
                "почему ищет работу",
                "поиск вакансии",
                "Aiva market",
            ],
            "sources": source("references/my-intro.md#L11"),
            "question": "Почему вы сейчас рассматриваете новые вакансии?",
            "answer": paragraphs[5],
            "supported_by": ["project:aiva-agent-platform"],
        },
    ]


def merge_drafts(
    existing: list[dict[str, Any]], generated: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], int]:
    generated_by_id = {record["id"]: record for record in generated}
    preserved: list[dict[str, Any]] = []
    protected = 0

    for record in existing:
        record_id = record.get("id")
        if record_id not in generated_by_id:
            preserved.append(record)
            continue
        if record.get("publication_status") != "draft":
            preserved.append(record)
            generated_by_id.pop(record_id)
            protected += 1

    merged_generated = [
        record for record in generated if record["id"] in generated_by_id
    ]
    return [*merged_generated, *preserved], protected


def build_knowledge_base(existing: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    generated = core_records()
    interview_records, duplicate_numbers = parse_interview_questions()
    generated["interview_qa"] = [*interview_records, *intro_interview_records()]

    result = dict(existing)
    protected = 0
    for collection in COLLECTIONS:
        merged, collection_protected = merge_drafts(
            existing.get(collection, []), generated[collection]
        )
        result[collection] = merged
        protected += collection_protected

    summary = {
        "generated": {name: len(generated[name]) for name in COLLECTIONS},
        "duplicate_question_numbers_skipped": duplicate_numbers,
        "non_draft_records_preserved": protected,
        "total_records": sum(len(result[name]) for name in COLLECTIONS),
    }
    return result, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb", type=Path, default=DEFAULT_KB)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write the generated drafts to the knowledge base; otherwise preview only",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    existing = json.loads(args.kb.read_text(encoding="utf-8"))
    result, summary = build_knowledge_base(existing)
    changed = result != existing
    summary["changed"] = changed
    summary["written"] = bool(args.write and changed)

    if args.write and changed:
        args.kb.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
