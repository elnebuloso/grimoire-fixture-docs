# FastAPI documentation

- Upstream: https://github.com/fastapi/fastapi, branch `master`
- Commit: `1ca09c13584ca45aa0921e5e40b31d49c5e3135a`
- Copied on 2026-11-07
- Source paths for grimoire: `vendor/fastapi/docs/en/docs` (English), `vendor/fastapi/docs/de/docs`
  (German)
- License: MIT, see `LICENSE`

## What was copied

The Markdown files below `docs/en`, `docs/en/mkdocs.yml`, the Markdown files below `docs/de/docs`
and `LICENSE`. The German pages were added on 2026-11-07 from the same commit; upstream has no
`docs/de/mkdocs.yml` at that commit, so the German source has no `nav`. Left out: the other
languages, `docs/de/llm-prompt.md` (the translation prompt, not documentation), images, `docs_src` and everything else. The Markdown is unchanged. FastAPI embeds its
example code with its own `{* ../../docs_src/… *}` syntax, which grimoire does not resolve: those
lines stay as text, and `docs_src` is therefore not copied.
