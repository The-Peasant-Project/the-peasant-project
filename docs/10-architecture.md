---
id: 10-architecture
title: Architecture
part: 10
status: stub
audience: [practitioner, technical]
tags: [architecture, scheduler, ledger, node, api]
summary: The five components — node image, scheduler, ledger, buyer API, adapters — and how they fit together with no central server.
agent_guidance: Everything must run from one repository on one machine. Any component that requires a central service is a design error.
open_questions:
  - Draft this document.
depends_on: []
---

# Architecture

Components: the node image (container runtime, metering, heat and power telemetry); the scheduler (takes price, solar, heat demand, job queue and reciprocity score, decides what to run); the ledger (append-only, tamper-evident, implements the waterfall, the sweep and the reciprocity score); the buyer API (a plain compute-rental endpoint that hides everything else); adapters (interchangeable connections to DePIN networks and direct buyers). Discovery is peer-to-peer with a manual fallback.

```mermaid
flowchart TB
    Buyer[Buyers] --> API[Buyer API]
    API --> Sched[Scheduler]
    Price[Price feed] --> Sched
    Tele[Node telemetry: power, heat, solar] --> Sched
    Recip[Reciprocity score] --> Sched
    Sched --> Node[Node image: isolated containers]
    Node --> Meter[Metering]
    Meter --> Ledger[Ledger: waterfall, sweep, score]
    Ledger --> Recip
    Ledger --> Pay[Payouts: hosts, dividend, pool, fund]
    Adapters[DePIN and direct-buyer adapters] --> API
    Peers[Other nodes, peer to peer] <--> Sched
```
