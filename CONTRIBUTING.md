# Contributing

Humans and AI agents follow the same rules. The rules live in three places and nowhere else.

`AGENTS.md` says what the project is, what it must never become, and the design constants. Read it first.

`guides/` holds the house style: `explainer.md` for anything that teaches, `deliberation.md` for working through hard questions, `decisions.md` for how a rule changes.

`INDEX.md` is generated. Do not edit it by hand; run `python scripts/build_index.py`.

## The short version

1. Got a qualm, question or idea? Drop a file in `inbox/` using the template there. That is a contribution.
2. Changing a document? Keep its frontmatter accurate and add any new claim to the hand-waving register.
3. Changing a rule or a design constant? Open a deliberation, and finish with a decision log entry. Nothing else changes a rule, including an AI proposing it.
4. Every pull request runs the consistency check. It reads your change against the constants and the index and comments on contradictions. Fix them or argue in the PR.
5. Nothing merges itself. A human merges.

## Environment

Open the repo in GitHub Codespaces, or run the devcontainer locally with Docker. Same file, same environment. `make docs` serves the site, `make index` rebuilds the index, `make check` runs the consistency check locally if you have an API key set.
