---
id: 11-scheduler
title: "Spec: energy-and-reciprocity-aware scheduler"
part: 11
status: stub
audience: [practitioner, technical]
tags: [spec, scheduler, python, strands]
summary: The scheduler decides, on a short cycle, how much compute to run and which jobs to take, given energy price, local solar, heat demand at the site, the job queue, a grid-draw ceiling and the reciprocity score.
agent_guidance: Python. Pure decision logic separated from I/O so it can be tested without hardware. Strands Agents SDK may wrap it as an agent later; the core is a plain function.
open_questions:
  - Draft this document.
depends_on: []
---

# Spec: energy-and-reciprocity-aware scheduler

Inputs: current and forecast energy price; local solar output; site heat demand and current temperature; job queue with value, deadline and tolerance for interruption; grid-draw ceiling for the period; reciprocity score of this group and of peers offering work.

Output: a plan for the next cycle: which jobs run, at what power level, and whether to accept new work.

Constraints: never exceed the grid-draw ceiling; prefer curtailed or negative-priced energy; prefer jobs whose heat is wanted now; prefer work from higher-reciprocity peers; degrade gracefully when any input is missing.

Acceptance tests, in plain words: given a negative price and idle heat demand, the scheduler runs at maximum; given a price spike, it drops interruptible jobs first; given a grid-draw ceiling already hit, it refuses new work regardless of price; given two equal jobs from peers with different reciprocity scores, it takes the higher one; given no price feed at all, it falls back to a conservative default and logs it.

Interfaces: a single plan(state) -> Plan function with typed inputs; a thin adapter layer for price feeds, telemetry and the job queue; a simulator that replays historical Victorian price data so the logic can be tested against real curtailment patterns.
