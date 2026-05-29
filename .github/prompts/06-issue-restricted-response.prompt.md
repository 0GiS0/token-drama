---
name: "06 Issue Restricted Response"
description: "Demo with hard limits: issue in 1 sentence + 3 bullets"
argument-hint: "Issue to analyze"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Analyze the issue and respond with these exact rules:

- Always refer the response to issue 1.
- Line 1: a single sentence (maximum 20 words).
- Then exactly 3 bullets.
- Each bullet must start with a verb in infinitive form.
- Do not add any extra text before or after.
