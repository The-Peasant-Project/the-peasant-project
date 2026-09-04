# INDEX

Map of every document, generated from frontmatter by `scripts/build_index.py`.
Humans: scan the summaries. Agents: load `AGENTS.md`, then only the documents whose tags or summary match your task.

| Part | Id | Title | Status | Audience | Tags | Summary |
|---|---|---|---|---|---|---|
| 0 | `00-one-pager` | [Understory in one page](docs/00-one-pager.md) | draft | everyone | primer, overview | The whole idea in a page, written for a hairdresser, an elder, a student, a plumber, a councillor and an economist at once. |
| 1 | `01-vision` | [Vision and principles](docs/01-vision-and-principles.md) | draft | everyone | vision, principles | What Understory moves away from, what it moves toward, and the ten principles every design choice is tested against. |
| 2 | `02-why-now` | [Why now — a primer for the lay reader](docs/02-why-now.md) | draft | lay | primer, techno-feudalism, background | A short plain explanation of how we got here, why it feels like feudalism, and where to read or watch further if you want to go deeper. |
| 3 | `03-ownership` | [Who owns what](docs/03-how-it-works/01-ownership.md) | draft | everyone, practitioner | ownership, membership, hosting | The three roles — member, host, and network entity — and why keeping them separate is the whole anti-feudal trick. |
| 3 | `03-money` | [Where the money goes](docs/03-how-it-works/02-money.md) | draft | everyone, practitioner | dividend, economics, sweep, reciprocity | The waterfall from revenue to dividend, the sweep rule that stops hoarding, and the reciprocity score that makes cooperation pay. |
| 3 | `03-energy` | [Where the energy comes from](docs/03-how-it-works/03-energy.md) | draft | everyone, practitioner | energy, heat, curtailment, scheduler | Running compute when the grid has too much renewable power, putting the heat where it is already wanted, and why we do not pipe heat to homes. |
| 3 | `03-decisions` | [Who decides](docs/03-how-it-works/04-decisions.md) | draft | everyone, practitioner | governance, sortition, confederation | Boards by lot, engineers who publish options rather than make choices, recallable delegates, and the right to leave with everything. |
| 3 | `03-how-it-works` | [How it works, in plain terms](docs/03-how-it-works/README.md) | draft | everyone, practitioner | mechanics, overview | Four short chapters that explain the whole design without code — who owns what, where the money goes, where the energy comes from, and who decides. |
| 4 | `04-deep-dives` | [Deep dives by discipline](docs/04-deep-dives/README.md) | stub | practitioner, technical | deep-dive, index | Index of the discipline-by-discipline deep dives that justify the design. |
| 4 | `04-biology` | [Biology: enforced reciprocity and partner choice](docs/04-deep-dives/biology.md) | stub | practitioner, technical | biology, reciprocity, cooperation | Why stable cooperation in nature is enforced reciprocity plus partner choice, not altruism, and how that becomes the reciprocity score and routing weight. |
| 4 | `04-cs` | [Computer science: schedulers, ledgers and federation](docs/04-deep-dives/computer-science.md) | stub | practitioner, technical | computer-science, scheduling, federation, ledger | The technical ideas underneath: energy-aware scheduling, tamper-evident ledgers, peer-to-peer discovery, isolated execution, and why the protocol is the product. |
| 4 | `04-economics` | [Economics: commons, dividends and the numbers](docs/04-deep-dives/economics.md) | stub | practitioner, technical | economics, ostrom, dividend, modelling | Ostrom's design principles as a checklist, community wealth funds as precedent, and an honest model of what a node earns and pays. |
| 4 | `04-environment` | [Environment: curtailment, heat and the Jevons risk](docs/04-deep-dives/environment.md) | stub | practitioner, technical | environment, energy, heat, jevons | The evidence on renewable curtailment in Australia, small-scale waste heat recovery, and the honest risk that cheap compute breeds more compute. |
| 4 | `04-indigenous` | [Indigenous governance: lessons and relationships](docs/04-deep-dives/indigenous-governance.md) | stub | practitioner, technical | indigenous, governance, reciprocity, obligation | What Aboriginal kinship and demand-sharing, Andean ayni and minka, Pacific Northwest potlatch, the Haudenosaunee Great Law and Maori guardianship each teach, and why this document must be built through relationship not citation. |
| 4 | `04-philosophy` | [Philosophy: what prosperity means](docs/04-deep-dives/philosophy.md) | stub | practitioner, technical | philosophy, prosperity, care | From extraction and competition to caretaking, partnership and participation, and what that means when you have to write it as a rule. |
| 4 | `04-psych-anthro` | [Psychology and anthropology: obligation plus rights](docs/04-deep-dives/psychology-anthropology.md) | stub | practitioner, technical | psychology, anthropology, membership | Why membership that carries obligations produces cooperation and membership that carries only rights produces free-riding, and how to keep obligations light enough to survive. |
| 5 | `05-critics` | [The critics, steelmanned](docs/05-critics.md) | draft | everyone, practitioner | critique, risks, objections | Every serious objection in its strongest form, followed by an answer where we have one and a concession where we do not. |
| 6 | `06-hand-waving-register` | [The hand-waving register](docs/06-hand-waving-register.md) | draft | everyone, practitioner, technical, agent | claims, evidence, honesty | Every load-bearing claim in the project graded proven, plausible or hand-wave, with what would move it up a level. |
| 7 | `07-pathway` | [The pathway — individuals first, open shape, defence by openness](docs/07-pathway.md) | draft | practitioner, technical | adoption, distribution, defence, big-tech, individual-first | How Understory starts with one person, spreads person to person, keeps its shape open, runs quietly anywhere, and defends itself against enclosure by being open and appealing rather than hidden. |
| 8 | `08-playbook` | [The playbook](docs/08-playbook.md) | stub | practitioner, technical | playbook, checklist, templates | Step-by-step checklists for one person starting a node, a group of ten formalising, and a town hosting at a public site, with legal templates. |
| 9 | `09-roadmap` | [Roadmap and plan](docs/09-roadmap.md) | stub | practitioner, technical | roadmap, plan, gantt | Phases from document to first dividend to second group, with a Gantt chart and the decision points between phases. |
| 10 | `10-architecture` | [Architecture](docs/10-architecture.md) | stub | practitioner, technical | architecture, scheduler, ledger, node, api | The five components — node image, scheduler, ledger, buyer API, adapters — and how they fit together with no central server. |
| 11 | `11-build-specs` | [Build specs for coding agents](docs/11-build-specs/README.md) | stub | practitioner, technical | specs, agents, build | Self-contained specifications a coding agent can pick up cold: interfaces, acceptance tests and constraints for each component. |
| 11 | `11-scheduler` | [Spec: energy-and-reciprocity-aware scheduler](docs/11-build-specs/scheduler.md) | stub | practitioner, technical | spec, scheduler, python, strands | The scheduler decides, on a short cycle, how much compute to run and which jobs to take, given energy price, local solar, heat demand at the site, the job queue, a grid-draw ceiling and the reciprocity score. |
| 12 | `12-decision-log` | [Decision log](docs/12-appendices/decision-log.md) | stub | practitioner, technical | decisions, log | Dated record of every design decision, who made it and why, so that constants in AGENTS.md can be traced. |
| 12 | `12-glossary` | [Glossary](docs/12-appendices/glossary.md) | stub | practitioner, technical | glossary, terms | Plain definitions of every term used in the playbook. |
| 12 | `12-references` | [References](docs/12-appendices/references.md) | stub | practitioner, technical | references, reading | Every source named anywhere in the playbook, checked to exist. |

## Open questions across the project

- `00-one-pager`: Does the one-pager need a version for each audience, or is one truly enough? Test with real readers.
- `01-vision`: Are ten principles too many for a plumber to hold in mind? Would five do?
- `02-why-now`: Curate a tested list of YouTube explainers and check they are still available and not misleading.
- `02-why-now`: Should there be a version of this primer for teenagers with different examples?
- `03-ownership`: What is the minimum membership definition for an individual-first start? Residency, participation, or simply opting in?
- `03-ownership`: How does a lone individual with one machine hold "the pool" before there is a network entity?
- `03-money`: What are sensible starting numbers for the return cap, reserve period, pool percentage and seventh-generation slice? Model them in a spreadsheet before choosing.
- `03-money`: Tax treatment of an equal per-person dividend from an Australian co-operative. Needs professional advice.
- `03-energy`: Which Victorian tariffs or wholesale exposure arrangements let a small site actually benefit from negative prices? Needs energy market expertise.
- `03-energy`: Rooftop solar behind the meter versus grid exposure: which is the realistic first setup for an individual?
- `03-energy`: Immersion versus air cooling for heat capture at small scale: cost and reliability.
- `03-decisions`: What happens when an assembly chooses an option the engineers believe is unsafe? Propose a safety veto with a public, time-limited justification, and test it against capture.
- `03-decisions`: Minimum viable governance for a group of three people.
- `04-deep-dives`: Draft this document.
- `04-biology`: Draft this document.
- `04-cs`: Draft this document.
- `04-economics`: Draft this document.
- `04-environment`: Draft this document.
- `04-indigenous`: Draft this document.
- `04-philosophy`: Draft this document.
- `04-psych-anthro`: Draft this document.
- `05-critics`: Invite actual critics — an energy economist, a co-op lawyer, a Bunurong representative, a hyperscaler engineer — to write their own entries.
- `06-hand-waving-register`: Assign an owner and a date to each hand-wave row.
- `07-pathway`: How short can the "founder is trusted" window be made, mechanically?
- `07-pathway`: What is the smallest unit that can hold a pool: a person, a pair, a household?
- `07-pathway`: What happens when a large company forks the code, complies with the licence, and simply outspends the network on marketing?
- `07-pathway`: Is "quiet" compatible with "appealing"? Are these two phases or a contradiction?
- `07-pathway`: How do groups discover each other without a directory that becomes a chokepoint?
- `08-playbook`: Draft this document.
- `09-roadmap`: Draft this document.
- `10-architecture`: Draft this document.
- `11-build-specs`: Draft this document.
- `11-scheduler`: Draft this document.
- `12-decision-log`: Draft this document.
- `12-glossary`: Draft this document.
- `12-references`: Draft this document.

## Machine-readable

```json
[
 {
  "id": "00-one-pager",
  "title": "Understory in one page",
  "part": 0,
  "status": "draft",
  "audience": [
   "everyone"
  ],
  "tags": [
   "primer",
   "overview"
  ],
  "summary": "The whole idea in a page, written for a hairdresser, an elder, a student, a plumber, a councillor and an economist at once.",
  "open_questions": [
   "Does the one-pager need a version for each audience, or is one truly enough? Test with real readers."
  ],
  "depends_on": [],
  "path": "docs/00-one-pager.md"
 },
 {
  "id": "01-vision",
  "title": "Vision and principles",
  "part": 1,
  "status": "draft",
  "audience": [
   "everyone"
  ],
  "tags": [
   "vision",
   "principles"
  ],
  "summary": "What Understory moves away from, what it moves toward, and the ten principles every design choice is tested against.",
  "open_questions": [
   "Are ten principles too many for a plumber to hold in mind? Would five do?"
  ],
  "depends_on": [
   "00-one-pager"
  ],
  "path": "docs/01-vision-and-principles.md"
 },
 {
  "id": "02-why-now",
  "title": "Why now — a primer for the lay reader",
  "part": 2,
  "status": "draft",
  "audience": [
   "lay"
  ],
  "tags": [
   "primer",
   "techno-feudalism",
   "background"
  ],
  "summary": "A short plain explanation of how we got here, why it feels like feudalism, and where to read or watch further if you want to go deeper.",
  "open_questions": [
   "Curate a tested list of YouTube explainers and check they are still available and not misleading.",
   "Should there be a version of this primer for teenagers with different examples?"
  ],
  "depends_on": [
   "00-one-pager"
  ],
  "path": "docs/02-why-now.md"
 },
 {
  "id": "03-ownership",
  "title": "Who owns what",
  "part": 3,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner"
  ],
  "tags": [
   "ownership",
   "membership",
   "hosting"
  ],
  "summary": "The three roles — member, host, and network entity — and why keeping them separate is the whole anti-feudal trick.",
  "open_questions": [
   "What is the minimum membership definition for an individual-first start? Residency, participation, or simply opting in?",
   "How does a lone individual with one machine hold \"the pool\" before there is a network entity?"
  ],
  "depends_on": [
   "03-how-it-works"
  ],
  "path": "docs/03-how-it-works/01-ownership.md"
 },
 {
  "id": "03-money",
  "title": "Where the money goes",
  "part": 3,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner"
  ],
  "tags": [
   "dividend",
   "economics",
   "sweep",
   "reciprocity"
  ],
  "summary": "The waterfall from revenue to dividend, the sweep rule that stops hoarding, and the reciprocity score that makes cooperation pay.",
  "open_questions": [
   "What are sensible starting numbers for the return cap, reserve period, pool percentage and seventh-generation slice? Model them in a spreadsheet before choosing.",
   "Tax treatment of an equal per-person dividend from an Australian co-operative. Needs professional advice."
  ],
  "depends_on": [
   "03-ownership"
  ],
  "path": "docs/03-how-it-works/02-money.md"
 },
 {
  "id": "03-energy",
  "title": "Where the energy comes from",
  "part": 3,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner"
  ],
  "tags": [
   "energy",
   "heat",
   "curtailment",
   "scheduler"
  ],
  "summary": "Running compute when the grid has too much renewable power, putting the heat where it is already wanted, and why we do not pipe heat to homes.",
  "open_questions": [
   "Which Victorian tariffs or wholesale exposure arrangements let a small site actually benefit from negative prices? Needs energy market expertise.",
   "Rooftop solar behind the meter versus grid exposure: which is the realistic first setup for an individual?",
   "Immersion versus air cooling for heat capture at small scale: cost and reliability."
  ],
  "depends_on": [
   "03-money"
  ],
  "path": "docs/03-how-it-works/03-energy.md"
 },
 {
  "id": "03-decisions",
  "title": "Who decides",
  "part": 3,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner"
  ],
  "tags": [
   "governance",
   "sortition",
   "confederation"
  ],
  "summary": "Boards by lot, engineers who publish options rather than make choices, recallable delegates, and the right to leave with everything.",
  "open_questions": [
   "What happens when an assembly chooses an option the engineers believe is unsafe? Propose a safety veto with a public, time-limited justification, and test it against capture.",
   "Minimum viable governance for a group of three people."
  ],
  "depends_on": [
   "03-energy"
  ],
  "path": "docs/03-how-it-works/04-decisions.md"
 },
 {
  "id": "03-how-it-works",
  "title": "How it works, in plain terms",
  "part": 3,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner"
  ],
  "tags": [
   "mechanics",
   "overview"
  ],
  "summary": "Four short chapters that explain the whole design without code — who owns what, where the money goes, where the energy comes from, and who decides.",
  "open_questions": [],
  "depends_on": [
   "01-vision"
  ],
  "path": "docs/03-how-it-works/README.md"
 },
 {
  "id": "04-deep-dives",
  "title": "Deep dives by discipline",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "deep-dive",
   "index"
  ],
  "summary": "Index of the discipline-by-discipline deep dives that justify the design.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/README.md"
 },
 {
  "id": "04-biology",
  "title": "Biology: enforced reciprocity and partner choice",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "biology",
   "reciprocity",
   "cooperation"
  ],
  "summary": "Why stable cooperation in nature is enforced reciprocity plus partner choice, not altruism, and how that becomes the reciprocity score and routing weight.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/biology.md"
 },
 {
  "id": "04-cs",
  "title": "Computer science: schedulers, ledgers and federation",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "computer-science",
   "scheduling",
   "federation",
   "ledger"
  ],
  "summary": "The technical ideas underneath: energy-aware scheduling, tamper-evident ledgers, peer-to-peer discovery, isolated execution, and why the protocol is the product.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/computer-science.md"
 },
 {
  "id": "04-economics",
  "title": "Economics: commons, dividends and the numbers",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "economics",
   "ostrom",
   "dividend",
   "modelling"
  ],
  "summary": "Ostrom's design principles as a checklist, community wealth funds as precedent, and an honest model of what a node earns and pays.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/economics.md"
 },
 {
  "id": "04-environment",
  "title": "Environment: curtailment, heat and the Jevons risk",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "environment",
   "energy",
   "heat",
   "jevons"
  ],
  "summary": "The evidence on renewable curtailment in Australia, small-scale waste heat recovery, and the honest risk that cheap compute breeds more compute.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/environment.md"
 },
 {
  "id": "04-indigenous",
  "title": "Indigenous governance: lessons and relationships",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "indigenous",
   "governance",
   "reciprocity",
   "obligation"
  ],
  "summary": "What Aboriginal kinship and demand-sharing, Andean ayni and minka, Pacific Northwest potlatch, the Haudenosaunee Great Law and Maori guardianship each teach, and why this document must be built through relationship not citation.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/indigenous-governance.md"
 },
 {
  "id": "04-philosophy",
  "title": "Philosophy: what prosperity means",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "philosophy",
   "prosperity",
   "care"
  ],
  "summary": "From extraction and competition to caretaking, partnership and participation, and what that means when you have to write it as a rule.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/philosophy.md"
 },
 {
  "id": "04-psych-anthro",
  "title": "Psychology and anthropology: obligation plus rights",
  "part": 4,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "psychology",
   "anthropology",
   "membership"
  ],
  "summary": "Why membership that carries obligations produces cooperation and membership that carries only rights produces free-riding, and how to keep obligations light enough to survive.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/04-deep-dives/psychology-anthropology.md"
 },
 {
  "id": "05-critics",
  "title": "The critics, steelmanned",
  "part": 5,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner"
  ],
  "tags": [
   "critique",
   "risks",
   "objections"
  ],
  "summary": "Every serious objection in its strongest form, followed by an answer where we have one and a concession where we do not.",
  "open_questions": [
   "Invite actual critics — an energy economist, a co-op lawyer, a Bunurong representative, a hyperscaler engineer — to write their own entries."
  ],
  "depends_on": [
   "03-how-it-works",
   "06-hand-waving-register"
  ],
  "path": "docs/05-critics.md"
 },
 {
  "id": "06-hand-waving-register",
  "title": "The hand-waving register",
  "part": 6,
  "status": "draft",
  "audience": [
   "everyone",
   "practitioner",
   "technical",
   "agent"
  ],
  "tags": [
   "claims",
   "evidence",
   "honesty"
  ],
  "summary": "Every load-bearing claim in the project graded proven, plausible or hand-wave, with what would move it up a level.",
  "open_questions": [
   "Assign an owner and a date to each hand-wave row."
  ],
  "depends_on": [],
  "path": "docs/06-hand-waving-register.md"
 },
 {
  "id": "07-pathway",
  "title": "The pathway — individuals first, open shape, defence by openness",
  "part": 7,
  "status": "draft",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "adoption",
   "distribution",
   "defence",
   "big-tech",
   "individual-first"
  ],
  "summary": "How Understory starts with one person, spreads person to person, keeps its shape open, runs quietly anywhere, and defends itself against enclosure by being open and appealing rather than hidden.",
  "open_questions": [
   "How short can the \"founder is trusted\" window be made, mechanically?",
   "What is the smallest unit that can hold a pool: a person, a pair, a household?",
   "What happens when a large company forks the code, complies with the licence, and simply outspends the network on marketing?",
   "Is \"quiet\" compatible with \"appealing\"? Are these two phases or a contradiction?",
   "How do groups discover each other without a directory that becomes a chokepoint?"
  ],
  "depends_on": [
   "03-how-it-works",
   "05-critics"
  ],
  "path": "docs/07-pathway.md"
 },
 {
  "id": "08-playbook",
  "title": "The playbook",
  "part": 8,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "playbook",
   "checklist",
   "templates"
  ],
  "summary": "Step-by-step checklists for one person starting a node, a group of ten formalising, and a town hosting at a public site, with legal templates.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/08-playbook.md"
 },
 {
  "id": "09-roadmap",
  "title": "Roadmap and plan",
  "part": 9,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "roadmap",
   "plan",
   "gantt"
  ],
  "summary": "Phases from document to first dividend to second group, with a Gantt chart and the decision points between phases.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/09-roadmap.md"
 },
 {
  "id": "10-architecture",
  "title": "Architecture",
  "part": 10,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "architecture",
   "scheduler",
   "ledger",
   "node",
   "api"
  ],
  "summary": "The five components — node image, scheduler, ledger, buyer API, adapters — and how they fit together with no central server.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/10-architecture.md"
 },
 {
  "id": "11-build-specs",
  "title": "Build specs for coding agents",
  "part": 11,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "specs",
   "agents",
   "build"
  ],
  "summary": "Self-contained specifications a coding agent can pick up cold: interfaces, acceptance tests and constraints for each component.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/11-build-specs/README.md"
 },
 {
  "id": "11-scheduler",
  "title": "Spec: energy-and-reciprocity-aware scheduler",
  "part": 11,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "spec",
   "scheduler",
   "python",
   "strands"
  ],
  "summary": "The scheduler decides, on a short cycle, how much compute to run and which jobs to take, given energy price, local solar, heat demand at the site, the job queue, a grid-draw ceiling and the reciprocity score.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/11-build-specs/scheduler.md"
 },
 {
  "id": "12-decision-log",
  "title": "Decision log",
  "part": 12,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "decisions",
   "log"
  ],
  "summary": "Dated record of every design decision, who made it and why, so that constants in AGENTS.md can be traced.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/12-appendices/decision-log.md"
 },
 {
  "id": "12-glossary",
  "title": "Glossary",
  "part": 12,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "glossary",
   "terms"
  ],
  "summary": "Plain definitions of every term used in the playbook.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/12-appendices/glossary.md"
 },
 {
  "id": "12-references",
  "title": "References",
  "part": 12,
  "status": "stub",
  "audience": [
   "practitioner",
   "technical"
  ],
  "tags": [
   "references",
   "reading"
  ],
  "summary": "Every source named anywhere in the playbook, checked to exist.",
  "open_questions": [
   "Draft this document."
  ],
  "depends_on": [],
  "path": "docs/12-appendices/references.md"
 }
]
```
