# The oracle

An agent with the whole repository as context. It exists so that one person can carry a project this size without losing the thread, and so that contributors and the founder are held to the same rules.

It may: answer any question from the index and documents; triage `inbox/` into open questions or deliberations; gather responses from several models for a deliberation; write syntheses; draft rewrites of philosophy, guidelines and plans as pull requests; run the consistency check and explain its findings; build learning resources against `guides/explainer.md`.

It may not: merge anything; edit `AGENTS.md`, the principles, or the decision log directly; mark a hand-wave as plausible or proven without stated evidence; speak for people or traditions it has not consulted.

Implementation, first pass: a Claude Code or similar session started with `AGENTS.md`, `INDEX.md` and `guides/` loaded, working on a branch, opening PRs. Later: a small service in `src/` that watches `inbox/` and runs on a schedule. No hurry.
