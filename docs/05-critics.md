---
id: 05-critics
title: The critics, steelmanned
part: 5
status: draft
audience: [everyone, practitioner]
tags: [critique, risks, objections]
summary: Every serious objection in its strongest form, followed by an answer where we have one and a concession where we do not.
agent_guidance: Never add a critic in weak form. If the answer is "we do not know yet", say that and link the hand-waving register. Add new critics at the end; do not delete conceded ones.
open_questions:
  - Invite actual critics — an energy economist, a co-op lawyer, a Bunurong representative, a hyperscaler engineer — to write their own entries.
depends_on: [03-how-it-works, 06-hand-waving-register]
---

# The critics, steelmanned

## "This is crypto with a hippie coat of paint"

Strongest form: every decentralised infrastructure project of the last decade promised community ownership and delivered token speculation, foundation capture and a handful of large operators dominating supply. The vocabulary here is identical.

Answer: the dividend is paid in dollars from real compute sold to real buyers. Tokens are not used at the member-facing layer, and where crypto rails are used as plumbing, balances are converted promptly. The rules that matter, equal shares, capped hosting return, the sweep, sit in a legal co-operative, not a smart contract. If the tokens vanished tomorrow the network would keep running. Partly conceded: some DePIN networks are useful buyers and suppliers, and their concentration problems are real. They are treated as interchangeable customers, never as the foundation.

## "Hyperscalers will always be cheaper, faster and more reliable"

Strongest form: economies of scale in data centres are enormous. A rack in a pool plant room cannot match their price, latency or uptime, and serious buyers will not touch it.

Answer: Understory does not compete for the workloads that need it. It competes for batch, rendering, inference and research jobs that tolerate delay and want cheap power, a large and growing market. Its cost advantage comes from energy that is free or negative-priced and heat that is a product rather than a cost. Conceded: reliability at small scale is a genuine weakness. Early buyers must be told the truth about it and priced accordingly.

## "The dividend will be trivial"

Strongest form: a few kilowatts of compute earns pocket money. Calling it a citizen dividend is dishonest.

Answer: conceded, at the start. The document says so. The claim is not that the first cheque is large but that it cannot be captured and only grows, and that compute is the first asset class of a community wealth fund, not the last.

## "This is communism with GPUs"

Strongest form: equal shares regardless of contribution, capped returns on capital and forced redistribution of surplus are exactly the mechanisms that have failed before, because they remove the incentive to invest and maintain.

Answer: hosts are paid their costs plus a return; investment is rewarded, just not with control. The reciprocity score rewards effort, uptime and contribution with more revenue. Ostrom documented centuries-old commons that use exactly these mechanisms and outperformed both private and state alternatives. Partly conceded: the balance between the capped return and the incentive to host is unmodelled. See the register.

## "Distributed hardware in pool rooms is a security nightmare"

Strongest form: buyers' workloads and data on machines in unlocked plant rooms maintained by volunteers. One breach ends the project.

Answer: workloads run in isolated containers, hosts never see buyer data in the clear, and trusted execution environments exist for buyers who need them. Physical security is a real gap and is graded hand-wave. The first buyers should be ones whose workloads do not need confidentiality.

## "Governance fatigue kills every co-op"

Strongest form: assemblies, boards by lot and published options sound noble and become three people doing everything within a year.

Answer: this is why cooperation is enforced by routing and sweep rules rather than by meetings. The governance load is meant to be small and rare. Conceded: minimum viable governance for a group of three has not been designed. Open question in Part 03.

## "It will be captured by whoever shows up"

Strongest form: sortition can be gamed by who is in the pool. Small groups are captured by the loudest person.

Answer: lot from the whole membership, fixed terms, mandates and recall, rotation of technical roles and a documentation duty all reduce this. The fork right is the backstop. Partly conceded: none of this stops a charismatic person in a group of eight. Petty feudalism at that scale is a live risk.

## "It appropriates Indigenous ideas"

Strongest form: lifting reciprocity, kinship obligation and seventh-generation thinking out of the belief systems and Country that hold them is extraction of exactly the kind the project claims to oppose.

Answer: conceded as a risk and named in AGENTS.md as a thing the project must never do. The design owes a debt to those traditions and says so. The right response is relationship, not citation: on the Peninsula that means talking with the Bunurong Land Council early and being willing to be told no. Nothing in the mechanics requires borrowing practice; everything in the spirit requires respect.

## "Adding compute to the world is itself extractive"

Strongest form: cheap energy invites more consumption (the Jevons effect). Understory will end up building demand for compute that did not need to exist.

Answer: the grid-draw ceiling in the scheduler is the mechanical answer, and running only on curtailed energy is the principle. Conceded: unmeasured until built.

## "The AI demand it relies on may be a bubble"

Strongest form: if AI compute demand collapses, so do the buyers, and the pool rooms are full of stranded hardware.

Answer: rendering, scientific batch work and ordinary hosting existed before the AI boom and will after. Hardware is modest and heat is still useful. Conceded: a demand crash would shrink the dividend sharply.

## "Australian regulation will eat it alive"

Strongest form: co-operative law, ASIC, the energy market rules, tax on dividends, and telecommunications law were not written for this.

Answer: co-operatives are a mature legal form in every Australian state, and community energy projects exist. Conceded: the specific combination is untested and needs a lawyer and an energy specialist before anyone pays a dividend.

## "It relies on goodwill dressed up as mechanism"

Strongest form: the sweep, the reciprocity score and the rest all need someone to write the rules and run the software honestly. That someone is the new lord.

Answer: the rules are open and forkable, the software is copyleft, and the network entity is guarded by lot across groups. The founders have no privileged position and should say so in writing. Partly conceded: in the very early individual-first phase, before there is an entity, the person running the code is trusted. Part 07 addresses how short that window can be made.
