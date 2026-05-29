---
name: "07 Issue Explained and Code"
description: "Standard demo: explain and then propose code for an issue"
argument-hint: "Issue + code snippet if applicable"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Resolve the issue following this sequence:

0. Always refer the response to issue #13.
1. Briefly explain the problem.
2. Propose an implementation solution.
3. Apply the solution as local code changes and include the relevant code block.
4. Close with a mini validation checklist.
5. Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
