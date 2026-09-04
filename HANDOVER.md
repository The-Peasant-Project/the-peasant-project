# HANDOVER — 4 September 2026 (evening)

Read this first. It supersedes anything in the repo that contradicts it. Update it before you stop.

## The one sentence

We are making a kit that lets one competent person run the everyday online tools their neighbours already pay for, as a co-op they can't take over.

The kit is three things: the software bundle (websites, bookings, email, files, one login, one bill, export button, on one server), the playbook (how twenty customers become a co-op with fair rules), and the guides (the ladder that turns a curious person into someone who can run the server). Software, rules, teaching. Nothing else is the product.

Everything else in the repo is a proof the kit works (demos), a place it will eventually run (Understory hardware), or the reason it should exist (philosophy, critics, deep dives). Keep those, but do not build them first.

## How the thinking moved today

Started as a federated compute network (Understory) with a citizen dividend. Realised nobody wants infrastructure; they want their bills lower and their tools owned. Reframed to Tools first: "everything Squarespace does, but yours." Understory is now phase 4. Then realised the real wedge is not a box but a person: a local sysadmin running services for twenty neighbours as a co-op. That is the kit.

## Build 1, the only thing for the next three months

One rented server (Australian provider, not a hyperscaler; Binary Lane suggested, about AUD 10 to 15 a month). Rob is the person. FatNumbat Media (Rob's own creative business: music and art prints) is customer one. Done means:

- The Peasant Project site served from that server, GitHub demoted to mirror.
- FatNumbat's website, shop, email and files running on the bundle.
- A written before-and-after: what FatNumbat paid, to how many companies; what it pays now, to whom.
- An export that actually works: everything moved to a second server (a temporary one is fine) and back, timed.
- Backups offsite, tested by restoring once.
- Notes kept throughout, because they become the guides.

Open deliberation to settle by doing: Coop Cloud versus assembling our own from containers. Try Coop Cloud first for a weekend on this server. `deliberations/2026-09-04-build-on-coop-cloud.md`.

## Repo work, in priority order

1. Cut `README.md` to the one sentence, the three parts of the kit, and a link to `BUILD-1.md`. Create `BUILD-1.md` in the root with the done-list above.
2. Fix the website. It was rendering unstyled. The fix is the deploy-pages workflow with `.nojekyll` and Pages source set to "GitHub Actions". Confirm the Material theme and Mermaid diagrams render. (Once Build 1 lands the site moves to the co-op server anyway.)
3. Create `howto/` with the guide ladder and a template built to `guides/explainer.md`. The ladder, in order: own your first thing (photos off Google); an old laptop is a server; your own cloud at home (Nextcloud); reach it from anywhere safely (Tailscale or WireGuard); a website you own; bookings for your business (Cal.com); backups or none of this counts; run it for your neighbours; email, honestly. Rule: no guide is published until someone has followed it on real hardware. Draft rung one only.
4. Create `demos/` with a README listing the five demonstrations and what each proves: the switch (FatNumbat before and after), the harvest (simulated 20-member co-op through the ledger for a year), the afternoon (move a business between servers on a stopwatch), our own house (site off GitHub), the warm pool (later, needs hardware). Build order: switch, harvest, afternoon, house.
5. Merge the latest zip changes if not already done: rewritten `docs/00-one-pager.md` (opens with Jess the hairdresser, follows the explainer guide), rewritten `docs/01-vision-and-principles.md` (four components: Tools, Commons, Harvest, Ground), new `docs/02b-the-tools.md` (the product line, service table, build-versus-bundle), flipped `docs/09-roadmap.md`, and the decision log entries for the reframe.
6. Test `scripts/consistency_check.py` once `ANTHROPIC_API_KEY` is a repo secret. Set or disable the Codeberg mirror workflow.
7. Later, not now: the economics model behind demo two, the one-pager tested on three strangers, the first deliberation run properly.

## Things decided today (all in the decision log)

Umbrella name The Peasant Project; Understory is the hardware component only. Monorepo; split only on separate release cadence or contributors. Licences: CC BY-SA 4.0 docs, AGPL-3.0 code, plus a trademark policy to write. Borrowed scaffolding (GitHub, Codespaces, commercial models) is acceptable with a mirror and an exit. Rules change only via deliberation and decision log, for humans, oracle and agents alike. Tools first, Ground last. Use existing open source for services; build only the glue.

## Rules for the agent

Read `AGENTS.md`, then `guides/`. Plain English before technical. No bolded-header bullet lists. New claims go in the hand-waving register. Rule changes go through the decision log; agents get no exception. Branch, PR, never merge. Run `python scripts/build_index.py` after touching docs. Rewrite this file before ending.

## Paste-ready starting prompt

> Read `HANDOVER.md`, then `AGENTS.md`, then `INDEX.md`. In five lines, tell me what the kit is and what Build 1's done-list is. Then do repo task 1 (README and BUILD-1.md) and open a PR. Don't touch design constants without asking.
