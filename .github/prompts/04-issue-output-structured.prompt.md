---
name: "04 Issue Output Structured"
description: "Demo with format: issue in comparative action table"
argument-hint: "Issue to analyze"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Implement the fix for issue #13 as local code changes, then summarize ONLY with this structure:

Always refer the content to issue #13.

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
- Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
