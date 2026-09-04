# AGENTS.md — steering primer for any AI agent working on The Peasant Project

Load this before touching anything. Every document under `docs/` also carries its own `agent_guidance` in frontmatter; read that too when working inside a part.

## What this is

The Peasant Project is the umbrella. Understory is its first piece: the compute network and protocol. Read `guides/` before editing anything: `explainer.md` for anything that teaches, `deliberation.md` and `decisions.md` for how rules change, `oracle.md` if you are acting as the oracle.

## What Understory is

A playbook and protocol for small, community-owned compute networks. People and towns own modest compute hardware placed where its waste heat is useful and where cheap or curtailed renewable energy is available. The compute is rented to real buyers for real money. The earnings are split equally per person among members, with hosting costs and a capped return paid to whoever provides hardware. Surplus that sits still is swept to a shared pool that funds the next node somewhere else. Cooperation is rewarded by the routing layer itself, not by rules people have to remember.

## What Understory must never become

- A platform. If there is a company that everyone must go through, we have failed. It is a protocol and a playbook.
- A token project. Crypto rails may be used as plumbing where they are cheaper than banks. The dividend must never depend on a token price.
- A place where owning more hardware buys more governance or a bigger dividend. Hosting is paid at cost plus a capped return. Governance is per person. Dividend is per person.
- Dependent on goodwill. Every mechanism must work when people are selfish. Goodwill is the output.
- Dependent on any central server, including any run by the founders. Anyone must be able to copy the repo and run the whole thing alone.
- A borrowing of Indigenous ideas as mechanics. Lessons and relationships, yes. Lifting practices out of kin, place and belief, no.

## How to work here

- Plain English before technical detail, always. A hairdresser and an economist should both be able to read Part 00 to 03.
- Do not add bolded-header bullet lists. Short paragraphs and simple lists only.
- Every load-bearing claim you add goes into `docs/06-hand-waving-register.md` graded proven, plausible or hand-wave. If you cannot grade it, it is a hand-wave.
- Every critic you can imagine goes into `docs/05-critics.md` in their strongest form before you answer them. Conceding is allowed and expected.
- Every open question goes into the `open_questions` list in the relevant document's frontmatter, not buried in prose.
- Diagrams are Mermaid, inline, so they render on GitHub and the site and can be edited by agents.
- Update `INDEX.md` whenever you add, rename or materially change a document. Run `scripts/build_index.py` if it exists; otherwise edit by hand.
- Australian context first (co-operative law, the NEM energy market, Bunurong Country on the Mornington Peninsula) but nothing should be Australia-only by design.
- Do not invent references. If you cannot name the source, say so.

## Frontmatter schema

```yaml
id: 03-money            # unique, matches filename
title: Where the money goes
part: 3
status: draft | stub | reviewed
audience: [everyone | lay | practitioner | technical | agent]
tags: [dividend, economics]
summary: one sentence a human or an agent can use to decide whether to open this
agent_guidance: what an agent should know or avoid when editing this file
open_questions:
  - question one
depends_on: [ids]
```

## Design constants (change only by decision log entry)

- Dividend: equal per member, non-transferable, non-inheritable, lapses on exit.
- Hosting return cap: cost plus a modest fixed percentage, set by assembly, never by the host.
- Hosting concentration cap: no household above a set share of any pool's compute.
- Sweep: undistributed, uninvested surplus flows to the shared pool after a fixed period.
- Reciprocity score drives routing weight. Score falls, routing falls. No human adjudication.
- Seventh-generation fund: fixed slice of all yield, unspendable by the assembly that raised it.
- Board by lot. Delegates recallable. Engineers publish options with costs; assemblies choose.
- Right to exit: data, node, and protocol are portable. The fork button always exists.
