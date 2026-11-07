# grimoire-fixture-docs

Documentation fixtures that grimoire syncs and indexes for development and testing. Every element
grimoire processes appears here at least once, with the result grimoire is expected to produce,
so a deviation is visible at a glance.

When grimoire's page on writing documentation (`docs/handbook/writing.md` in the grimoire
repository) gains a feature, add an example of it here and the expected result to this README.

## Sources

The repository holds two documentation sites; each is one source. Both sync over `https` without
credentials.

| Source path | Site config | Git URL | Branch |
|---|---|---|---|
| `zensical/docs` | `zensical/zensical.toml` | `https://github.com/elnebuloso/grimoire-fixture-docs` | `main` |
| `mkdocs/docs` | `mkdocs/mkdocs.yml` | `https://github.com/elnebuloso/grimoire-fixture-docs` | `main` |

`shared/` lies outside both source paths. Pages include files from it, so grimoire has to fetch
it besides the source path.

The IDs below are written as `<project>/<source>/…`; with a project `fixtures` and sources named
`zensical` and `mkdocs`, `<project>/<source>/glossary` is `fixtures/zensical/glossary`.

A sync of either source ends with no error and no warnings. The dead links listed below are the
only ones.

## `zensical/docs`

Demonstrates:

- `zensical.toml` with `nav`, and `glossary.md` left out of it
- `toc` `separator = "_"` with the default slugify
- front matter with `title`, `description` and `tags`
- content tabs
- a whole include and partial includes (lines `3:5`, named section `main`) from `shared/`
- an include from inside the source path (`snippets/ports.txt`)
- Mermaid
- a page with only an overview
- a section merged into its parent
- a section split into two parts
- relative links with and without anchor, a link to the same page, and dead links

Pages in index order, with their snippets:

| Page | Title | Snippet anchors |
|---|---|---|
| `index.md` | Platform handbook (from front matter, tags `platform`, `operations`) | overview, `getting_access_to_the_platform`, `installing_platformctl`, `where_to_ask_for_help` |
| `auth-service.md` | Auth service | overview, `deploying_the_auth_service`, `ports_of_the_platform_services`, `rotating_the_signing_keys` |
| `runbooks/rollback.md` | Rolling back a deploy | overview, `when_to_roll_back` (alias `who_decides`), `how_the_rollback_works`, `rolling_back_step_by_step` in two parts `(1/2)` and `(2/2)`, `after_a_rollback` |
| `glossary.md` | Glossary (not in `nav`) | overview only |

Notable results:

- `<project>/<source>/auth-service#deploying_the_auth_service` contains the caution from
  `shared/caution.md` as `> **Caution:** …`, lines 3 to 5 of `shared/commands.md`, and only
  `def main` from `shared/deploy.py`, without the `--8<--` markers.
- `<project>/<source>/auth-service#ports_of_the_platform_services` contains the table from
  `snippets/ports.txt`.
- `<project>/<source>/index#installing_platformctl` contains the tabs as `**Linux:**` and
  `**macOS:**`.
- `<project>/<source>/runbooks/rollback#how_the_rollback_works` keeps the Mermaid diagram as a
  code block.
- `### Who decides` is too short to stand alone and is merged into `when_to_roll_back`.

Dead links:

| On page | Section | Link | Why |
|---|---|---|---|
| `index.md` | `where_to_ask_for_help` | `services.md` | missing page |
| `auth-service.md` | `rotating_the_signing_keys` | `auth-service.md#token-lifetime` | missing anchor |
| `runbooks/rollback.md` | `when_to_roll_back` | `../../shared/caution.md` | leaves the source path |

## `mkdocs/docs`

Demonstrates:

- `mkdocs.yml` with `nav`, and `notes/oncall.md` left out of it
- `toc` `slugify` set to `pymdownx.slugs.slugify` with `case: lower`, which keeps umlauts in IDs
- admonitions: with a title, with an empty title, and collapsible (`???+`)
- content tabs
- images with and without alt text
- HTML comments on one line and over several lines
- a page without a title
- a reference-style link whose definition sits in another section
- dead links

Pages in index order, with their snippets:

| Page | Title | Snippet anchors |
|---|---|---|
| `index.md` | Billing | overview, `monatlicher-abrechnungslauf`, `zahlungsläufe-prüfen`, `who-to-contact` |
| `invoices.md` | Invoices | overview, `correcting-an-invoice`, `payment-provider-outages` |
| `notes/oncall.md` | `notes/oncall` (no H1, not in `nav`) | overview, `payment-provider-down`, `billing-run-failed` |

Notable results:

- The overview of `index.md` contains the image's alt text. The image without alt text and both
  HTML comments are gone.
- `<project>/<source>/index#monatlicher-abrechnungslauf` contains the untitled note as a plain
  `>` quote.
- `<project>/<source>/index#zahlungsläufe-prüfen` contains the collapsible tip as
  `> **Faster check:** …`, and its own copy of the definition `[corrections]`, pointing at
  `<project>/<source>/invoices#correcting-an-invoice`.

Dead links:

| On page | Section | Link | Why |
|---|---|---|---|
| `invoices.md` | `payment-provider-outages` | `refunds.md` | missing page |
| `invoices.md` | `payment-provider-outages` | `invoices.md#late-fees` | missing anchor |
| `invoices.md` | `payment-provider-outages` | `../shared/caution.md` | leaves the source path |

## `vendor/`: documentation that is not ours

Copies of eight public documentations, four in English and four in German, at a fixed commit, for
grimoire's benchmark: the same input on every run, whatever happens upstream. Each folder has the upstream license and a `VENDOR.md` with
the upstream repository, the commit, what was copied and what was changed.

| Folder | Source path for grimoire | Pages | Generator |
|---|---|---|---|
| `vendor/kubernetes` | `vendor/kubernetes/content/en` | 2,520 | Hugo |
| `vendor/mkdocs-material` | `vendor/mkdocs-material/docs` | 85 | MkDocs |
| `vendor/fastapi` | `vendor/fastapi/docs/en/docs` | 156 | MkDocs |
| `vendor/zensical` | `vendor/zensical/docs` | 57 | Zensical |
| `vendor/kubernetes` | `vendor/kubernetes/content/de` | 147 | Hugo |
| `vendor/fastapi` | `vendor/fastapi/docs/de/docs` | 125 | MkDocs |
| `vendor/i-doit` | `vendor/i-doit/docs/de` | 725 | MkDocs |
| `vendor/odoo-wiki` | `vendor/odoo-wiki` | 930 | Zensical |

The folders are updated only on purpose, as a whole, with a new commit in their `VENDOR.md`; the
benchmark's baseline changes with them. The sources of the agent environment above do not read
`vendor/`.
