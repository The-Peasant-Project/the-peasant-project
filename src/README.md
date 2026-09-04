# Code

Monorepo by decision (see decision log, 2026-09-04). Each package here has its own README, tests and, when it matters, its own container. Split a package into its own repo only when it has its own release cadence or its own contributors.

- `understory-scheduler/` — energy-and-reciprocity-aware scheduler. Spec: `docs/11-build-specs/scheduler.md`. Python, pure decision logic first, Strands wrapper later.
- `understory-ledger/` — append-only ledger implementing the waterfall, sweep and reciprocity score. Spec to be written.
