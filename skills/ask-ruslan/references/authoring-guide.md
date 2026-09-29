# Knowledge-base authoring

Use this guide only when maintaining the Ask Ruslan knowledge base.

## Publication workflow

1. Add new facts to `knowledge-base.json` with `publication_status: "draft"`. When importing the bundled `my-intro.md` and `typical-questions.md` sources, run `python3 scripts/import_markdown_drafts.py --write` from the skill directory. The importer collapses duplicate questions, preserves unrelated records, and never overwrites a non-draft record.
2. Keep each record narrow enough that Ruslan can approve every factual claim in it.
3. Record provenance in `sources`. Use a short non-secret reference; never copy credentials, private contact details, confidential client material, or unpublished source contents into the public base.
4. Ask Ruslan to review the exact record. Approval of one record does not approve related inferences or other records.
5. Only after explicit approval, set `publication_status` to `approved_public` and add `approved_on` and `approved_by`.
6. Run `python3 scripts/search_knowledge.py --validate-only`.

The Markdown files are provenance sources, not searchable knowledge by themselves. Only records in `knowledge-base.json` whose status is `approved_public` are returned by the search script. Re-running the importer updates generated drafts but preserves records that have already been approved, made private, or retired.

Use `private` only as an exclusion marker. A public plugin should normally store private material elsewhere rather than embedding it in this bundle. Use `retired` when a previously public record must no longer appear in answers.

## Record design

- IDs are stable lowercase kebab-case identifiers, unique across all four collections.
- `tags` are broad controlled topics, such as `backend`, `architecture`, or `leadership`.
- `keywords` contain exact terms and common synonyms a user may type.
- `technologies` contain product, language, framework, protocol, or platform names.
- Outcomes must be factual and sourced. Do not turn estimates into measured results.
- Curated interview answers should reference their factual basis with `supported_by` when they rely on experience, projects, or principles.
- An interview answer may have an empty `supported_by` only when it is itself directly approved and its `sources` document that approval.

## Minimal shapes

All records also require the base fields defined in `knowledge-base.schema.json`: `id`, `publication_status`, `title`, `tags`, `keywords`, and `sources`.

- Experience adds `summary`, `responsibilities`, and `outcomes`; organization, role, period, and technologies are optional because they may be sensitive.
- Project adds `problem`, `ruslan_contribution`, `decisions`, and `outcomes`.
- Principle adds `statement` and `application`; `exceptions` is optional.
- Interview Q&A adds `question`, `answer`, and `supported_by`.

The checked-in base intentionally contains no factual example records. Examples can be accidentally presented as real experience, so test data belongs in temporary files only.
