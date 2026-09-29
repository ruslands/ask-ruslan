#!/usr/bin/env python3

import importlib.util
import json
import unittest
from copy import deepcopy
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("import_markdown_drafts.py")
SPEC = importlib.util.spec_from_file_location("import_markdown_drafts", MODULE_PATH)
assert SPEC and SPEC.loader
IMPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMPORTER)

SEARCH_MODULE_PATH = Path(__file__).with_name("search_knowledge.py")
SEARCH_SPEC = importlib.util.spec_from_file_location(
    "search_knowledge_for_import_test", SEARCH_MODULE_PATH
)
assert SEARCH_SPEC and SEARCH_SPEC.loader
SEARCH = importlib.util.module_from_spec(SEARCH_SPEC)
SEARCH_SPEC.loader.exec_module(SEARCH)


class ImportMarkdownDraftsTests(unittest.TestCase):
    def empty_knowledge_base(self):
        return {
            "schema_version": "1.0.0",
            "owner_display_name": "Ruslan",
            "publication_policy": {
                "default_status": "draft",
                "searchable_status": "approved_public",
                "notes": "test",
            },
            "experience": [],
            "projects": [],
            "principles": [],
            "interview_qa": [],
        }

    def test_question_import_collapses_known_duplicates(self):
        records, duplicate_numbers = IMPORTER.parse_interview_questions()
        self.assertEqual(len(records), 31)
        self.assertEqual(duplicate_numbers, [6, 14])

    def test_generated_records_are_unique_drafts(self):
        result, summary = IMPORTER.build_knowledge_base(self.empty_knowledge_base())
        records = [
            record
            for collection in IMPORTER.COLLECTIONS
            for record in result[collection]
        ]
        self.assertEqual(summary["total_records"], 40)
        self.assertEqual(len({record["id"] for record in records}), 40)
        self.assertTrue(
            all(record["publication_status"] == "draft" for record in records)
        )
        available_references = {
            f"{kind}:{record['id']}"
            for kind, collection in (
                ("experience", "experience"),
                ("project", "projects"),
                ("principle", "principles"),
            )
            for record in result[collection]
        }
        used_references = {
            reference
            for record in result["interview_qa"]
            for reference in record["supported_by"]
        }
        self.assertLessEqual(used_references, available_references)

    def test_non_draft_record_is_never_overwritten(self):
        knowledge_base = self.empty_knowledge_base()
        protected = deepcopy(IMPORTER.core_records()["projects"][0])
        protected.update(
            {
                "publication_status": "approved_public",
                "approved_on": "2026-09-29",
                "approved_by": "Ruslan",
                "title": "Reviewed title",
            }
        )
        knowledge_base["projects"] = [protected]

        result, summary = IMPORTER.build_knowledge_base(knowledge_base)
        matching = [
            record
            for record in result["projects"]
            if record["id"] == protected["id"]
        ]
        self.assertEqual(matching, [protected])
        self.assertEqual(summary["non_draft_records_preserved"], 1)

    def test_import_is_idempotent(self):
        first, _ = IMPORTER.build_knowledge_base(self.empty_knowledge_base())
        second, _ = IMPORTER.build_knowledge_base(json.loads(json.dumps(first)))
        self.assertEqual(first, second)

    def test_representative_queries_work_after_explicit_approval(self):
        knowledge_base, _ = IMPORTER.build_knowledge_base(
            self.empty_knowledge_base()
        )
        for collection in IMPORTER.COLLECTIONS:
            for record in knowledge_base[collection]:
                record.update(
                    {
                        "publication_status": "approved_public",
                        "approved_on": "2026-09-29",
                        "approved_by": "Ruslan",
                    }
                )

        cases = (
            ("Какой опыт у Руслана с голосовыми агентами?", "interview_qa:interview-28"),
            ("Расскажите про Backend-Driven UI в Самокате", "project:samokat-backend-driven-ui"),
            ("Как Руслан использует spec-driven development?", "principle:spec-driven-ai-development"),
            ("Какой у Руслана опыт с RAG и pgvector?", "interview_qa:interview-25"),
        )
        for query, expected_reference in cases:
            with self.subTest(query=query):
                result = SEARCH.search(knowledge_base, query, None, 5, 2)
                references = [match["ref"] for match in result["matches"]]
                self.assertIn(expected_reference, references)


if __name__ == "__main__":
    unittest.main()
