---
name: "05 Issue: Analysis and local changes"
description: "Open demo: full response for an issue"
argument-hint: "Issue to analyze"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Analyze the issue and deliver a complete response, then implement the fix as local code changes.

Include:

- Always reference the analysis to issue #13.
- Diagnosis
- Solution plan
- Risks and mitigations
- Next steps
- Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
