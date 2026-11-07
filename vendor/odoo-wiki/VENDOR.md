# Odoo Wiki (German)

- Upstream: https://github.com/Mint-System/Odoo-Wiki, branch `main`
- Commit: `f7dddafe65767a81fcceefdc630ebdf8c30c958b`
- Copied on 2026-11-07
- Source path for grimoire: `vendor/odoo-wiki`
- License: AGPL-3.0, see `LICENSE`

## What was copied

The Markdown files at the root of the repository, `zensical.toml` and `LICENSE`. Left out:
`attachments/`, `docs/` (only assets there), the build scripts and everything else. The Markdown
is unchanged; template expressions such as `{{ $frontmatter.description }}`, which the upstream
build fills in, stay as text. The upstream `README.md` and `AGENTS.md` are pages of this source,
as they lie beside the others.
