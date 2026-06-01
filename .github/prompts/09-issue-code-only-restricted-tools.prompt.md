---
name: "09 Issue Code Only – Restricted Tools"
description: "Token savings demo: code only, with minimal tool set"
argument-hint: "Issue + tech stack + target file"
agent: "agent"
model: Claude Sonnet 4.6 (copilot)
tools: [vscode, execute, read, edit, search, web, browser, todo]
---

Solve the issue #13 by applying local code changes, and respond with code ONLY.

Rules:

- Do not include natural language explanations.
- Keep the code minimal to solve the issue.
- Local changes only: never commit, push, or create issues or PRs, so the work can be reverted to test another prompt.
- Use GitHub CLI to get the issue details
