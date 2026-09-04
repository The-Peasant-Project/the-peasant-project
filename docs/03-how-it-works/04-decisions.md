---
id: 03-decisions
title: Who decides
part: 3
status: draft
audience: [everyone, practitioner]
tags: [governance, sortition, confederation]
summary: Boards by lot, engineers who publish options rather than make choices, recallable delegates, and the right to leave with everything.
agent_guidance: The engineer/assembly split is the classic technocracy trap. Do not soften the rule that engineers publish options with costs and assemblies choose.
open_questions:
  - What happens when an assembly chooses an option the engineers believe is unsafe? Propose a safety veto with a public, time-limited justification, and test it against capture.
  - Minimum viable governance for a group of three people.
depends_on: [03-energy]
---

# Who decides

Small groups become petty fiefdoms in two ways: someone becomes indispensable, or someone becomes invisible. Understory refuses both.

Boards are chosen by lot from members, the way juries are, for fixed terms. Delegates to any regional level carry written mandates and can be recalled by the group that sent them.

The people who run the machines do not make policy. They publish every significant decision as a set of options with costs and risks, in plain language, and the members choose. Technical roles rotate, are paid from a budget the assembly sets, and carry a duty to document everything so anyone can take over. Anyone can run a node from the published playbook.

Anyone can leave. Your node, your data and the protocol go with you. If the network ever turns into a landlord, you fork it.

```mermaid
flowchart TD
    Eng[Engineers] -- publish options with costs --> Ass[Assembly of members]
    Lot[Chosen by lot] --> Board
    Board -- runs day to day within mandate --> Ass
    Ass -- chooses --> Dec[Decision]
    Ass -- sends recallable delegate --> Reg[Regional confederation]
    Reg -- pool allocation, dispute resolution --> Ass
```

Larger towns can build larger nodes and keep most of what they earn. What they cannot do is convert size into control. Their delegate has one voice like everyone else's, and their pool contribution funds the next small town, which then adds capacity and buyers to the network they profit from.
