---
name: "08 Issue Code Only"
description: "Token savings demo: respond with code only"
argument-hint: "Issue + tech stack + target file"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
---

Solve the issue by applying local code changes, and respond with code ONLY.

Rules:

- Always reference the solution to issue #13.
- Do not include natural language explanations.
- If multiple files are needed, separate them with file path comments.
- Keep the code minimal to solve the issue.
- Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
