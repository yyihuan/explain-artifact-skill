# explain-artifact

A Markdown-first workflow for explanatory documents: reader analysis, reviewable narration and media design, then HTML presentation.

## Use

Install this repository as the `explain-artifact` skill in your agent’s supported skill directory. Start with [SKILL.md](SKILL.md).

The sample can be rebuilt locally with Python 3:

```sh
python3 examples/build.py
```

Open `examples/lesson.html` in a browser. The builder supports this small sample’s syntax, not arbitrary Markdown. Diagram assets remain relative local resources. The optional companion `document-diagrams` skill handles structure diagrams.

Optional Gemini rewriting is documented in [plain-language-rewrite.md](references/plain-language-rewrite.md): preserve the original, compare facts and qualifiers, then generate HTML from the accepted Markdown. Gemini 3.8 Flash with MEDIUM is the requested configuration; no real API call or writing-quality benchmark is claimed.

## Versions and provenance

- `v0.1.0`: snapshot of the existing local skill before this refresh. Personal absolute paths were normalized and caches excluded; original rules were retained. This tag was created during publication, not at the historical date the skill was first written.
- `v0.2.0`: the refreshed skill, with supporting references and examples.

## Verification and limits

Skill frontmatter checks passed. Diagram rendering and source freshness were checked, including rejection after source changes and recovery after rendering. References and sample HTML image paths were checked. Tests used the existing pinned local renderer installation. Clean-machine npm installation, browser visual review, screen-reader behavior and external Gemini execution have not been verified. The freshness check verifies source digest and renderer metadata, not arbitrary SVG edits or factual correctness.

No license is granted beyond applicable default rights for original material at this stage. External software and linked sources retain their own licenses; dependencies are not vendored.
