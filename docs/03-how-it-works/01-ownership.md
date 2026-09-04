---
id: 03-ownership
title: Who owns what
part: 3
status: draft
audience: [everyone, practitioner]
tags: [ownership, membership, hosting]
summary: The three roles — member, host, and network entity — and why keeping them separate is the whole anti-feudal trick.
agent_guidance: Never let host and member collapse into one privileged role. The separation is load-bearing.
open_questions:
  - What is the minimum membership definition for an individual-first start? Residency, participation, or simply opting in?
  - How does a lone individual with one machine hold "the pool" before there is a network entity?
depends_on: [03-how-it-works]
---

# Who owns what

Feudalism happens when the same party owns the land, runs it, and collects the money. Understory keeps those apart on purpose.

A member is a person. Every member holds exactly one share. It cannot be bought, sold, given away or inherited, and it lapses when you leave. Members vote, serve on boards when drawn by lot, and receive the dividend.

A host is whoever provides hardware, power or a site. A host might be a member, a club, a council, a school or a business. Hosts are paid their costs plus a capped return set by the assembly. Hosting does not earn extra votes or extra dividend. No single household may host more than a set share of any pool's compute.

The network entity is a legal body, a co-operative in Australia, that owns the shared pool, the protocol and the name. Its guardians are chosen by lot from across all member groups. It exists so that the commons has standing in court and so that no single group can capture it.

```mermaid
flowchart LR
    Member -- one share each --> Vote[Votes and dividend]
    Host -- hardware, power, site --> Paid[Costs + capped return]
    Entity[Network entity] -- holds --> Pool[Shared pool, protocol, name]
    Member -. may also be .-> Host
    Host -. never gains .-> Vote
```

When you start alone, you are all three at once. That is fine for one machine. The moment a second person joins, the roles separate and the rules above apply. Part 07 covers this transition.
