---
name: career-intelligence-copilot
description: Maintain a job-search intelligence workflow: refresh job-market data, merge normalized postings, analyze market structure, rank real companies, and reverse-engineer resume or portfolio improvements from real role requirements. Use when the user asks to update job postings, compare companies, analyze job-market signals, maintain a decision workbook, or turn real postings into career strategy.
---

# Career Intelligence Copilot

## Goal

Maintain one continuous workflow:

1. Collect real job postings.
2. Normalize them into a durable master dataset.
3. Analyze the current market.
4. Rank companies with transparent constraints.
5. Reverse-engineer resume, portfolio, and interview improvements from real postings.
6. Write conclusions into reports and a decision workbook.

Do not treat scraping, analysis, resume advice, and company ranking as unrelated tasks.

## Read First

Read:

- `references/file-map.md`
- `references/workbook-rules.md`

If the task involves master-dataset writes, also read:

- `references/master-dataset-merge.md`

If the task involves resume advice, capability gaps, or company ranking, also read:

- `references/real-role-derived-guidance.md`

If the task involves web access, use the project's browser or web-access workflow. If it involves spreadsheets, use the project's spreadsheet tooling.

## Public Workspace Contract

Recommended local inputs:

- `output/jobs_master.json`
- `output/jobs_master.csv`
- `workbook.xlsx`
- `private/resumes/*.pdf`
- `private/compensation.md`

Recommended generated outputs:

- `output/jobs_master.json`
- `output/jobs_master.csv`
- `output/job_market_report_YYYY-MM-DD.md`
- `output/personal_positioning_report_YYYY-MM-DD.md`
- `workbook.xlsx`

Private runtime state:

- `profile/`
- raw scraped data
- resumes
- offer notes
- compensation files
- generated reports from a real search

## Skill-First Execution

- Treat this skill as the workflow rule source.
- If a rule is written here, implement it as at least one executable guard:
  - pre-scrape check
  - post-scrape check
  - record filter
  - merge guard
  - stop-write condition
- Do not use ad hoc one-off scripts to overwrite the master dataset.
- For master-dataset writes, call the canonical merge script:
  - `scripts/merge_master_dataset.py`
  - or `scripts/run_merge_master.cmd`

## Scraping Rules

- Prefer a real browser and persistent login state for dynamic job boards.
- Before writing Boss Zhipin records, sample at least one detail page.
- If detail pages show missing salary, login-only descriptions, or incomplete recruiter information, stop and ask the user to log in.
- Support multiple search keywords and platform-specific target counts.
- Track:
  - `run_date`
  - `first_seen_date`
  - `last_seen_date`
  - `seen_count`
  - `seen_dates`

## Filtering Rules

Remove before incoming JSON and master merge:

- headhunter roles
- anonymous recommendation roles
- company names like `某上市公司`, `某新能源公司`, or other non-identifiable entities
- records with missing required fields
- company-name parsing noise such as `急聘`, `统招本科`, `本科`, `经验不限`, or salary ranges

If a company-name field looks like parsing noise, first try to recover the real company from the detail page, JSON-LD, company-info block, or company introduction. If it still cannot be recovered, drop the record.

## Master Dataset Rules

- Scraping output must first become a normalized incoming JSON array.
- Incoming rows must have required fields documented in `references/master-dataset-merge.md`.
- Merge through the safe merge script.
- The merge script must:
  - validate required fields
  - deduplicate incoming rows
  - preserve first/last seen metadata
  - back up current CSV and JSON before replacement
  - atomically write new files
  - reject suspicious baseline mismatches

## Market Analysis Rules

Do not only count postings. Analyze structure:

- company type
- company ownership
- asset side vs user side vs platform side
- role type
- salary band and total-pay certainty
- headquarters or base location
- travel or on-site requirements
- work-intensity signals
- platform differences

Salary conclusions should be decision-oriented:

- monthly salary range
- bonus months if available
- total-pay certainty
- whether higher pay is offset by commute, location, work intensity, or organizational ambiguity

## Company Ranking Rules

Use only companies that appear in the accepted master dataset.

Do not rank by salary alone. Combine:

- company ownership
- base location
- work intensity
- monthly salary
- bonus or total-pay certainty
- assets and moat
- resume value
- skill growth
- career stability
- overtime friendliness
- personal fit

Rank by buckets first:

- asset side
- user side
- technology / platform / solution side
- integrated energy / aggregation / retail side

Then produce practical recommendation levels such as:

- main target
- track closely
- watch
- avoid

## Workbook Rules

The workbook is a decision board, not a raw dump.

Short decision fields should appear first:

- company name
- representative role
- ownership
- business side
- base location
- work-intensity judgment
- pay judgment
- recommendation level

Long text should appear later:

- role characteristics
- responsibility summary
- recommendation reason
- main risks

## Resume Reverse-Engineering Rules

Resume advice must come from accepted real postings.

Extract:

- repeated capability tags
- representative companies and roles
- responsibilities that map to the user's current evidence
- capability gaps worth filling

Good advice connects role demand to concrete resume or portfolio evidence.

Avoid generic advice like "improve data ability" unless it is grounded in specific postings and role clusters.
