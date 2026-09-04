---
id: 03-energy
title: Where the energy comes from
part: 3
status: draft
audience: [everyone, practitioner]
tags: [energy, heat, curtailment, scheduler]
summary: Running compute when the grid has too much renewable power, putting the heat where it is already wanted, and why we do not pipe heat to homes.
agent_guidance: Lead with curtailed energy, not heating. Heat to homes is explicitly out of scope at the outset. Flag the Jevons risk honestly.
open_questions:
  - Which Victorian tariffs or wholesale exposure arrangements let a small site actually benefit from negative prices? Needs energy market expertise.
  - "Rooftop solar behind the meter versus grid exposure: which is the realistic first setup for an individual?"
  - "Immersion versus air cooling for heat capture at small scale: cost and reliability."
depends_on: [03-money]
---

# Where the energy comes from

On a sunny afternoon in Victoria there is often more solar power than anyone can use. Prices go to zero or below and rooftop systems get switched off. That wasted power is the fuel.

A node runs hardest when power is cheapest and throttles when it is dear. The scheduler decides, minute by minute, how much work to take and where. This is a well understood problem and the first real piece of software in Understory.

Computers turn almost all their electricity into heat. Instead of paying to get rid of it, the node sits where heat is wanted: the hot water system of an aged care home, the town pool, a greenhouse, a laundry. The site gets free heat. The node gets a cheap home.

We do not pipe heat to houses. Distribution is hard, seasonal and expensive. Put the compute at the heat load, and distribute money instead.

```mermaid
flowchart LR
    Price[Grid price feed] --> S[Scheduler]
    Solar[Local solar] --> S
    Demand[Heat demand at site] --> S
    Jobs[Job queue from buyers] --> S
    S --> Run[Run more or less compute]
    Run --> Heat[Heat into water or air at site]
```

## The honest caveat

Adding compute to the world uses energy, even cheap energy. If Understory only ever soaks up power that would otherwise be curtailed, it is close to free in environmental terms. If it starts drawing on the grid at peak to chase revenue, it becomes part of the problem. The scheduler must have a hard ceiling on grid-drawn energy that the assembly sets and the hosts cannot override. This is logged as a hand-wave until it is built and measured.
