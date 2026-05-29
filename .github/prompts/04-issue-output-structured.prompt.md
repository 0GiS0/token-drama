---
name: "04 Issue Output Structured"
description: "Demo with format: issue in comparative action table"
argument-hint: "Issue to analyze"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Analyze the issue and respond ONLY with this structure:

Always refer the content to issue #13

| Field                | Content             |
| -------------------- | ------------------- |
| Problem summary      | One sentence        |
| Suspected root cause | One sentence        |
| Evidence needed      | Max 3 short bullets |
| Proposed fix         | Max 3 short bullets |
| Risks                | Max 2 bullets       |
| Done when            | Verifiable criteria |

Rules:

- Do not add sections outside the table.
- If information is missing, write "Unknown" in the cell.
