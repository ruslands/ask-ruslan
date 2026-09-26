#!/usr/bin/env python3

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("search_knowledge.py")
SPEC = importlib.util.spec_from_file_location("search_knowledge", MODULE_PATH)
assert SPEC and SPEC.loader
SEARCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEARCH)


def record(record_id, status, keyword, *, approved=True):
    item = {
        "id": record_id,
        "publication_status": status,
        "title": f"Record {record_id}",
        "tags": ["backend"],
        "keywords": [keyword],
        "technologies": [],
        "sources": [{"type": "ruslan_statement", "reference": "test fixture"}],
        "problem": "A test problem",
        "ruslan_contribution": ["A test contribution"],
        "decisions": [],
        "outcomes": [],
    }
    if approved:
        item.update({"approved_on": "2026-09-15", "approved_by": "Ruslan"})
    return item


def knowledge_base(projects):
    return {
        "schema_version": "1.0.0",
        "owner_display_name": "Ruslan",
        "publication_policy": {
            "default_status": "draft",
            "searchable_status": "approved_public",
            "notes": "test",
        },
        "experience": [],
        "projects": projects,
        "principles": [],
        "interview_qa": [],
    }


class SearchKnowledgeTests(unittest.TestCase):
    def test_private_and_draft_records_are_never_returned(self):
        data = knowledge_base(
            [
                record("private-match", "private", "kubernetes", approved=False),
                record("draft-match", "draft", "kubernetes", approved=False),
            ]
        )
        result = SEARCH.search(data, "Kubernetes", None, 5, 0)
        self.assertEqual(result["public_records_considered"], 0)
        self.assertEqual(result["matches"], [])

    def test_approved_record_is_found_by_keyword(self):
        data = knowledge_base([record("public-match", "approved_public", "kubernetes")])
        result = SEARCH.search(data, "Опыт с Kubernetes", "project", 5, 2)
        self.assertEqual(result["matches"][0]["ref"], "project:public-match")
        self.assertGreaterEqual(result["matches"][0]["score"], 10)

    def test_equal_scores_sort_by_stable_reference(self):
        data = knowledge_base(
            [
                record("zeta", "approved_public", "kubernetes"),
                record("alpha", "approved_public", "kubernetes"),
            ]
        )
        result = SEARCH.search(data, "kubernetes", None, 5, 2)
        self.assertEqual(
            [match["ref"] for match in result["matches"]],
            ["project:alpha", "project:zeta"],
        )

    def test_public_record_requires_explicit_approval_metadata(self):
        data = knowledge_base(
            [record("unapproved-public", "approved_public", "kubernetes", approved=False)]
        )
        errors = SEARCH.validate_kb(data)
        self.assertTrue(any("lacks approved_on or approved_by" in error for error in errors))

    def test_short_keyword_does_not_match_inside_another_word(self):
        data = knowledge_base([record("go-project", "approved_public", "go")])
        result = SEARCH.search(data, "Django", None, 5, 2)
        self.assertEqual(result["matches"], [])

    def test_technology_punctuation_is_searchable(self):
        item = record("cpp-project", "approved_public", "systems")
        item["technologies"] = ["C++"]
        data = knowledge_base([item])
        result = SEARCH.search(data, "Опыт с C++", None, 5, 2)
        self.assertEqual(result["matches"][0]["ref"], "project:cpp-project")


if __name__ == "__main__":
    unittest.main()
