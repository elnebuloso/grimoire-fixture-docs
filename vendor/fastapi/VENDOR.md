# FastAPI documentation

- Upstream: https://github.com/fastapi/fastapi, branch `master`
- Commit: `1ca09c13584ca45aa0921e5e40b31d49c5e3135a`
- Copied on 2026-11-07
- Source path for grimoire: `vendor/fastapi/docs/en/docs`
- License: MIT, see `LICENSE`

## What was copied

The Markdown files below `docs/en`, `docs/en/mkdocs.yml` and `LICENSE`. Left out: the other
languages, images, `docs_src` and everything else. The Markdown is unchanged. FastAPI embeds its
example code with its own `{* ../../docs_src/… *}` syntax, which grimoire does not resolve: those
lines stay as text, and `docs_src` is therefore not copied.
