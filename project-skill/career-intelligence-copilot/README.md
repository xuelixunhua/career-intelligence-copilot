# career-intelligence-copilot

This is a project-local Codex skill for maintaining a job-market intelligence workflow.

It is useful when a job search needs recurring data refreshes, structured market analysis, company ranking, and resume updates derived from real postings.

## What It Does

1. Collect postings from job boards with a browser-first workflow.
2. Normalize scraped rows into an incoming JSON layer.
3. Filter headhunters, anonymous companies, parsing noise, and incomplete records.
4. Merge accepted rows into a guarded master dataset.
5. Generate market and personal-positioning reports.
6. Refresh a decision workbook for company comparison.

## Core Rules

- `SKILL.md` is the rule source.
- Rules written in the skill must map to executable checks, filters, or merge guards.
- Company ranking must use real accepted postings, not imagined target lists.
- Resume advice must be reverse-engineered from real role requirements.
- Long raw fields belong behind short decision fields in workbook views.
- Private data stays outside the public repository.

## Files

- `SKILL.md`: main workflow instructions.
- `references/file-map.md`: recommended workspace layout.
- `references/master-dataset-merge.md`: incoming JSON and merge-guard contract.
- `references/workbook-rules.md`: decision workbook structure.
- `references/real-role-derived-guidance.md`: how to derive resume and company decisions from postings.

## Scripts

The public repository keeps scripts in the repository-level `scripts/` folder:

- `scripts/merge_master_dataset.py`
- `scripts/run_merge_master.cmd`
- `scripts/update_weekly_job_market.example.py`

Project-specific browser scraping and login state should remain private.
