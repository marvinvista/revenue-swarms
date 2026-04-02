# Revenue Swarms

Parallel specialist workflows for revenue teams.

These swarms split hard GTM work into parallel specialist lanes, then return one decision-ready output.

They are especially useful for revenue teams that need better decisions before they need more headcount.

Each top-level folder is a portable swarm you can copy straight into `$CODEX_HOME/skills`.

## Install In 30 Seconds

Clone the repo and copy the swarm folder you want:

```bash
git clone https://github.com/marvinvista/revenue-swarms.git
mkdir -p "$CODEX_HOME/skills"
cp -R revenue-swarms/account-overview-swarm "$CODEX_HOME/skills/"
```

Then ask Codex to use the swarm by name.

<!-- GENERATED SWARMS START -->
## Swarms

### Narrative And Product Marketing

Use when you need a sharper story, clearer buyer language, and stronger problem-solution framing before doing more selling work.

| Swarm | Folder | Description |
| --- | --- | --- |
| Sales Narrative Swarm | `sales-narrative-swarm` | Build a sales narrative with buyer pain, value framing, proof, objections, and next actions. |

### Sales Materials

Use when you need to turn the core narrative into sales decks, demo structure, outreach assets, and other reusable selling materials.

| Swarm | Folder | Description |
| --- | --- | --- |
| Sales Materials Swarm | `sales-materials-swarm` | Turn the core sales narrative into practical decks, outreach assets, demo structure, proof packaging, and reusable collateral. |

### Prospecting

Use when you need to define who to target, what signals matter, and which accounts deserve attention now.

| Swarm | Folder | Description |
| --- | --- | --- |
| ICP Prospecting Swarm | `icp-prospecting-swarm` | Define the ideal customer profile, rank buying signals, and map likely entry points for outreach. |
| Pipeline Generation Swarm | `pipeline-generation-swarm` | Build a fresh ranked target-account plan for net-new pipeline using fit, timing, stakeholders, and outreach hypotheses. |
| Signal Monitoring To Action Swarm | `signal-monitoring-to-action-swarm` | Triage ongoing market and account signals into a ranked action queue for accounts or segments you already care about. |

### Account Research And Planning

Use when you need a compact account view before outreach, discovery, or deal work.

| Swarm | Folder | Description |
| --- | --- | --- |
| Account Overview Swarm | `account-overview-swarm` | Build a decision-ready account brief with verified facts, strategic context, stakeholder coverage, risks, and next actions. |

### Outreach And Appointment Setting

Use when you need more disciplined outbound, better hooks, and cleaner sequencing to earn first meetings.

| Swarm | Folder | Description |
| --- | --- | --- |
| Outbound Appointment Setting Swarm | `outbound-appointment-setting-swarm` | Plan outbound that books first meetings with stronger hooks, sharper CTAs, and cleaner sequencing. |

### Inbound Qualification

Use when you need to judge fit, urgency, and the right next step for inbound demand.

| Swarm | Folder | Description |
| --- | --- | --- |
| Inbound Qualification Swarm | `inbound-qualification-swarm` | Triage inbound demand, judge fit and urgency, and route the next step with more discipline. |

### Account Penetration

Use when you need coordinated multi-threading across a buying committee, not just one message.

| Swarm | Folder | Description |
| --- | --- | --- |
| Multi-Stakeholder Outreach Swarm | `multi-stakeholder-outreach-swarm` | Coordinate outreach across a buying committee with role-specific messaging, sequencing, and review boundaries. |

### Discovery, Demo, And Pitching

Use when you need stronger discovery, demo tailoring, objection handling, and meeting prep for an active opportunity.

| Swarm | Folder | Description |
| --- | --- | --- |
| Discovery Demo Swarm | `discovery-demo-swarm` | Prepare discovery and demo calls with tighter research, questions, objections, and follow-up. |

### Closing And Pipeline Management

Use when you need sharper deal judgment, close plans, and forecast realism once the work has moved down-funnel.

| Swarm | Folder | Description |
| --- | --- | --- |
| Deal Next Steps Swarm | `deal-next-steps-swarm` | Recommend the next best moves on an in-flight deal before it becomes a close or forecast review. |
| Closing Pipeline Swarm | `closing-pipeline-swarm` | Pressure-test late-stage close plans, commercial blockers, and forecast realism when commit judgment matters. |

### Customer Success

Use when you need stronger onboarding, adoption, renewal readiness, and expansion support after the deal is closed.

| Swarm | Folder | Description |
| --- | --- | --- |
| Customer Success Swarm | `customer-success-swarm` | Plan onboarding, adoption, renewal readiness, expansion support, and reference creation for early customers. |
<!-- GENERATED SWARMS END -->

## What A Swarm Looks Like

Each swarm lives in its own top-level folder:

```text
my-swarm/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
└── assets/
```

Only `SKILL.md` is required. Everything else is optional.

Codex compatibility note: swarms still use `SKILL.md` files and install into `$CODEX_HOME/skills`.
