---
name: "03 Freeform Issue Output"
description: "Unstructured demo: solve an issue with open output"
argument-hint: "Issue to analyze"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Resolve the issue specified by the user.

Instructions:

- Always refer the response to issue #13.
- Implement the fix as local code changes.
- Do not impose a fixed output structure.
- Prioritize clarity and usefulness for the team.
- Include actionable recommendations.
- Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
