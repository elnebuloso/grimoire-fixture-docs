# Zensical documentation

- Upstream: https://github.com/zensical/docs, branch `master`
- Commit: `48f313ef7f81db54fbbe8d58456d6875af78919f`
- Copied on 2026-11-07
- Source path for grimoire: `vendor/zensical/docs`
- License: MIT, see `LICENSE.md`

## What was copied

The Markdown files below `docs`, `mkdocs.yml`, `includes/` and `LICENSE.md`. Left out:
images, stylesheets, overrides and everything else.

## Changed

One include path: `docs/setup/language.md` includes `includes/languages.html` from the root of
the upstream repository, which here is `vendor/zensical/includes/languages.html`. The line was
changed to that path so it resolves from the root of this repository, as grimoire resolves
includes. The escaped `;--8<-- ".browserslistrc"` in `docs/authoring/code-blocks.md` is an
example, not an include, and stays.
