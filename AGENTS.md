# Project Instructions

## Skills
A skill is a set of local instructions to follow that is stored in a `SKILL.md` file. Below is the list of skills that can be used in this project only.

### Available skills
- import-weekly-issues: Create GitHub issues from a `weekN/weekN_issues_complete.csv` file and add them to a GitHub Project. Use this when the user explicitly asks to create or import issues for a specific `weekN` folder such as `week2` or `week10`. (file: /Users/sijun-yang/Documents/GitHub/SW-AI-W02-05-TEMPLATE/.codex/skills/import-weekly-issues/SKILL.md)

### How to use skills
- Discovery: The list above is the skills available in this project. Skill bodies live on disk at the listed paths.
- Trigger rules: If the user names a skill or the task clearly matches a skill's description shown above, you must use that skill for that turn.
- Missing/blocked: If a named skill is not in the list or the path cannot be read, say so briefly and continue with the best fallback.
- How to use a skill:
  1. After deciding to use a skill, open its `SKILL.md`.
  2. Read only enough to follow the workflow.
  3. Load extra referenced files only when needed.
- Safety and fallback: If a skill cannot be applied cleanly, state the issue, pick the next-best approach, and continue.
