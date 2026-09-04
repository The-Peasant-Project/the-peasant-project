---
id: 11-build-specs
title: Build specs for coding agents
part: 11
status: stub
audience: [practitioner, technical]
tags: [specs, agents, build]
summary: "Self-contained specifications a coding agent can pick up cold: interfaces, acceptance tests and constraints for each component."
agent_guidance: Each spec must be completable without reading the rest of the repo, but must link to AGENTS.md and the relevant Part 03 chapter. Include acceptance tests as plain statements before any code.
open_questions:
  - Draft this document.
depends_on: []
---

# Build specs for coding agents

Specs to write, in build order: scheduler, ledger, node image, buyer API, adapters, discovery. The scheduler spec is drafted first because it is the only genuinely novel component and the one the founder's skills fit.
