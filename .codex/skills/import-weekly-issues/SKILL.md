# Skill: Import Weekly Issues

## Description
Read a `weekN/weekN_issues_complete.csv` file, create GitHub issues, attach week/category/difficulty labels, and add them to a GitHub Project.

## Trigger
- The user explicitly asks to create issues for a specific `weekN`, such as `week2` or `week10`.
- Example requests: `week2 이슈 추가`, `week3 CSV로 이슈 만들어`, `week5 프로젝트에 올려`.
- If the user does not specify a `weekN`, ask which week to use and stop.

## Required Confirmation
- Never create issues or modify GitHub labels or a GitHub Project without explicit user approval.
- Before execution, run a dry-run summary and ask `이대로 진행할까요?`.

## Labeling Rules
- Week label: `week_N` based on the folder name, for example `week_2`.
- Category labels:
  - `category_common`
  - `category_basic`
  - `category_problem_solving`
  - `category_extra`
- Difficulty labels:
  - `difficulty_low`
  - `difficulty_medium`
  - `difficulty_high`
- Difficulty is applied only to problem-solving issues.
- Difficulty is inferred from `weekN/problem-solving/*.py` file names, not from the CSV.

## Workflow
1. Read `weekN/weekN_issues_complete.csv`.
2. Expect CSV columns `title,content`.
3. Run the helper script in dry-run mode:
   - `python3 .codex/skills/import-weekly-issues/scripts/import_weekly_issues.py weekN`
4. Show the user:
   - total issue count
   - category counts
   - difficulty counts
   - a preview of labels that will be applied
5. Ask `이대로 진행할까요?`.
6. After approval, execute:
   - `python3 .codex/skills/import-weekly-issues/scripts/import_weekly_issues.py weekN --execute`
7. The script will:
   - ensure missing labels exist in the repository
   - create issues with all calculated labels
   - add created issues to the configured GitHub Project
8. Report created issue count, project additions, and any failures.

## Project Filtering
- Use GitHub Project's built-in `Labels` field for filtering.
- Useful filters:
  - `label:week_2`
  - `label:week_2 label:difficulty_medium`
  - `label:category_extra`

## Implementation Notes
- Script path: `.codex/skills/import-weekly-issues/scripts/import_weekly_issues.py`
- Defaults:
  - project number: `1`
  - project owner: inferred from repo owner
- Optional flags:
  - `--repo owner/name`
  - `--owner OWNER`
  - `--project-number N`
  - `--skip-project-add`

## Constraints
- Do not guess the target project when multiple candidates exist.
- If one issue fails, continue safely when possible and report the failed items clearly.
