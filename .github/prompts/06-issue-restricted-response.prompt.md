---
name: "06 Issue Restricted Response"
description: "Demo with hard limits: issue in 1 sentence + 3 bullets"
argument-hint: "Issue to analyze"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Implement the fix for issue #13 as local code changes, then respond with these exact rules:

- Always refer the response to issue #13.
- Line 1: a single sentence (maximum 20 words).
- Then exactly 3 bullets.
- Each bullet must start with a verb in infinitive form.
- Do not add any extra text before or after.
- Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
