---
id: 03-money
title: Where the money goes
part: 3
status: draft
audience: [everyone, practitioner]
tags: [dividend, economics, sweep, reciprocity]
summary: The waterfall from revenue to dividend, the sweep rule that stops hoarding, and the reciprocity score that makes cooperation pay.
agent_guidance: Keep the waterfall order fixed unless a decision log entry changes it. Be honest that early dividends are small.
open_questions:
  - What are sensible starting numbers for the return cap, reserve period, pool percentage and seventh-generation slice? Model them in a spreadsheet before choosing.
  - Tax treatment of an equal per-person dividend from an Australian co-operative. Needs professional advice.
depends_on: [03-ownership]
---

# Where the money goes

Every dollar a node earns goes down the same waterfall, in the same order, every time.

First, hosts are paid what it cost them, plus the capped return. Second, a reserve is topped up for repairs and replacement. Third, a fixed slice goes to the seventh-generation fund, which the members who raised it cannot spend on themselves. Fourth, a percentage goes to the shared pool that funds new nodes elsewhere; that percentage rises gently as a group's yield grows, so bigger groups contribute more without being punished for size. Whatever is left is the dividend, split equally per member.

```mermaid
flowchart TD
    Rev[Revenue] --> H[1. Host costs + capped return]
    H --> Res[2. Reserve for repairs]
    Res --> Gen[3. Seventh-generation fund]
    Gen --> Pool[4. Shared pool, rising % with yield]
    Pool --> Div[5. Equal dividend per member]
```

## Wealth that must move

If a group leaves money in reserve beyond what repairs need, and does not distribute or reinvest it within a set period, it is swept to the shared pool automatically. Hoarding is not forbidden. It is pointless.

## Cooperation pays

Each group carries a reciprocity score. It rises when the group pays into the pool on time, keeps its nodes up, publishes its accounts and helps a new group start. It falls when it does not. The routing layer sends more work to groups with higher scores. Nobody has to argue, sanction or vote. A group that stops contributing simply earns less, and can earn it back by contributing again.

## Be honest about size

One node in one town will pay a dividend of tens or a few hundred dollars a year at first. That is not a living. It is a floor that only rises, because the rules do not allow it to be captured and the pool keeps building new nodes. Over time the network entity can hold other yield-bearing assets, shares in a solar farm, community housing, under the same equal-split rule. Compute is the first asset, not the only one.
