---
name: discovery-demo-swarm
description: "Run a multi-agent discovery and demo workflow that plans research, questions, demo tailoring, and objection handling for a live sales conversation. Use when the user wants stronger call prep rather than generic pitch advice."
---

# Discovery Demo Swarm

## Overview

Use this swarm to prepare for a discovery call, demo, or combined conversation where call quality matters.

This swarm combines research, discovery design, demo tailoring, and objection prep so the final plan helps the seller run a sharper meeting and a cleaner follow-up.

The job is not to script every sentence. The job is to improve the quality of the conversation.

## When to Use

- Use when the user is preparing for discovery, demo, or a live sales call.
- Use when the conversation needs both diagnosis and tailored product storytelling.
- Use when the output should help before, during, and immediately after the meeting.

## When Not to Use

- Do not use for top-of-funnel appointment setting.
- Do not use when the user only wants a generic product pitch.
- Do not use when the opportunity is already in close planning; route to a narrower swarm instead.

## Swarm Lanes

Launch four read-only sub-agents when the task is substantial enough that parallel work helps.

### Lane 1: Pre-Call Research Analyst

Ask this sub-agent to gather and organize:

- account or prospect context
- likely priorities
- relevant events or signals
- what the seller should know before the call

This lane should avoid speculative detail.

### Lane 2: Discovery Planner

Ask this sub-agent to design:

- discovery goals
- sequencing of questions
- diagnosis paths
- questions that expose urgency, pain, and current process

This lane should optimize for learning, not interrogation.

### Lane 3: Demo Tailoring Designer

Ask this sub-agent to define:

- what to show
- what to skip
- how to connect product capabilities to likely pains
- which proof points belong in the meeting

This lane should avoid defaulting to the same demo every time.

### Lane 4: Objection And Follow-Up Reviewer

Ask this sub-agent to anticipate:

- likely objections
- weak spots in the meeting plan
- follow-up needs
- next-step risks if the call goes well or poorly

This lane should keep the team honest about what the meeting can accomplish.

## Workflow

1. Define the meeting type and the outcome the seller wants.
2. Build a short intent packet:
   - account or prospect
   - meeting type and date
   - current deal stage if any
   - known stakeholders
   - known pain points or open questions
3. Launch the four read-only lanes in parallel.
4. Merge the work into one call plan.
5. End with a practical next-step plan for after the meeting.

## Output Contract

Return:

1. `Call Goal`
2. `Discovery Plan`
3. `Demo Focus`
4. `Likely Objections`
5. `Follow-Up Plan`
6. `Open Questions`

## Approval Boundaries

- Do not invent account context or stakeholder intent.
- Do not present guesses as confirmed call objectives.
- Do not send follow-up or calendar actions unless the user asks explicitly.

## Failure Shields

- Do not overload the meeting with too many themes.
- Do not let demo flow replace discovery.
- Do not use generic objection handling when the call context is specific.
- Do not produce a call plan with no next-step logic.
