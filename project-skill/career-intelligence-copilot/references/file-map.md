# File Map

This is the recommended private workspace layout for using the public skill.

## Public Skill Layer

- `project-skill/career-intelligence-copilot/SKILL.md`
  - workflow rules and trigger instructions

- `project-skill/career-intelligence-copilot/references/`
  - rule documents used by the skill

- `scripts/merge_master_dataset.py`
  - safe master-dataset merge entrypoint

- `scripts/update_weekly_job_market.example.py`
  - public scaffold for a weekly update orchestrator

## Private Data Layer

- `output/jobs_master.json`
  - canonical machine-readable master dataset

- `output/jobs_master.csv`
  - tabular mirror for checking and workbook import

- `tmp/incoming/jobs_YYYY-MM-DD.json`
  - normalized rows from the latest scrape before merge

- `tmp/incoming/merge_summary_YYYY-MM-DD.json`
  - merge result summary

## Decision Layer

- `workbook.xlsx`
  - decision workbook for market conclusions, personal positioning, company ranking, and interview questions

## Personal Material Layer

- `private/resumes/*.pdf`
  - private resume versions

- `private/compensation.md`
  - private compensation and offer constraints, if used

## Browser Runtime Layer

- `profile/`
  - persistent browser login state
  - never publish this directory

## Generated Reports

- `output/job_market_report_YYYY-MM-DD.md`
- `output/personal_positioning_report_YYYY-MM-DD.md`

Reports generated from a real search are private by default.
