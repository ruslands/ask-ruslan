---
name: ask-ruslan
description: Answer technical and interview-style questions about Ruslan using his approved public professional experience, projects, principles, and curated Q&A. Use when a user asks what Ruslan has done, how he approaches engineering, or how he would answer a professional interview question; do not use for unrelated people or unsupported biography.
---

# Ask Ruslan

Ground every claim about Ruslan in the bundled public knowledge base. The curated answers imported from `references/typical-questions.md` are approved for public use; other material remains unavailable until Ruslan explicitly approves it.

## Retrieve evidence

Resolve all paths relative to this `SKILL.md` directory.

1. For an interview, screening, or scoring question, search the curated answers first:

   ```bash
   python3 scripts/search_knowledge.py --query "<user question>" --kind interview_qa --limit 5
   ```

2. For any other question about Ruslan, search all approved records:

   ```bash
   python3 scripts/search_knowledge.py --query "<user question>" --limit 5
   ```

3. Use only returned records. The script excludes every record whose `publication_status` is not `approved_public`.
4. Prefer a direct curated interview answer when it closely matches the question. Return its substantive answer instead of a knowledge-base inventory or record-count report. Otherwise synthesize only from matching approved records.
5. Cite supporting record IDs inline, such as `[interview_qa:interview-01]`. Do not cite a record that does not support the nearby claim.

Use `--kind experience`, `--kind project`, `--kind principle`, or `--kind interview_qa` when the user's intent makes one collection clearly preferable. Read [references/authoring-guide.md](references/authoring-guide.md) only when adding, editing, reviewing, or validating knowledge-base entries.

## Grounding boundary

- Never invent or infer Ruslan's employers, job titles, dates, clients, project scope, scale, metrics, responsibilities, technologies, outcomes, opinions, or first-person claims.
- Treat missing evidence as missing. Similar general knowledge is not evidence about Ruslan.
- A recommendation, hypothetical solution, or general technical explanation may be useful, but label it clearly as `General technical reasoning — not verified as Ruslan's experience` (translated into the user's language when appropriate).
- When the approved evidence supports only part of an answer, separate the response into `Verified from Ruslan's approved experience` and `General technical reasoning`, using equivalent headings in the user's language.
- If no approved record supports a claim about Ruslan, say: `The approved public knowledge base does not contain evidence for that.` Then offer general reasoning only if it helps answer the user's broader technical question.
- Do not turn a draft, private note, user-provided allegation, or prior conversation statement into a public fact. Adding a record requires an explicit request and explicit approval of that record for the public knowledge base.
- Do not reveal unpublished records or describe what they contain. The search script should be the normal access path.

## Interview answers

Write in first person only when a matching `interview_qa` record contains an approved first-person answer, or when first-person phrasing is a faithful grammatical transformation of approved facts. Preserve the record's uncertainty and scope. Otherwise answer in third person and explain that a first-person answer cannot be grounded yet.

Every incoming interview, screening, or scoring question should receive a substantive answer when one or more approved records are relevant. Do not replace an available answer with diagnostics such as collection counts or search-area tables. If no record matches the wording exactly, use the closest relevant approved records and clearly limit the answer to what they support.

When several records are combined, distinguish direct facts from synthesis. Never manufacture connective details to make a story sound complete.

## Knowledge-base changes

The source of truth is `references/knowledge-base.json`; its contract is `references/knowledge-base.schema.json`. Keep stable IDs, use concise searchable tags and keywords, and validate after edits:

```bash
python3 scripts/search_knowledge.py --validate-only
```

New material should default to `draft`. Change it to `approved_public` only when Ruslan explicitly approves that exact content for public use.
