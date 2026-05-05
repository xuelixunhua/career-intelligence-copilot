# Career Intelligence Copilot

`Career Intelligence Copilot` is a project-local Codex skill for turning job-search research into a repeatable intelligence workflow.

It is designed for cases where job-search work is more than a list of openings:

- collect real postings from dynamic job boards
- normalize them into a durable master dataset
- filter headhunters, anonymous companies, and malformed records
- analyze market structure, pay bands, company types, and role patterns
- rank real companies with transparent decision criteria
- reverse-engineer resume and portfolio upgrades from real role requirements

The current public example uses Beijing power-trading roles from Boss Zhipin and Liepin, but the workflow is intentionally adaptable to other domains.

## What Changed In This Version

This repository now reflects the newer local workflow:

- the skill is treated as the rule source, not just documentation
- rules must map to executable checks, filters, or merge guards
- scraped rows are written to an `incoming` JSON layer before touching the master dataset
- master updates go through a strict merge script with backups and row-count guards
- anonymous companies, headhunter roles, and company-name parsing noise are removed before analysis
- company ranking is framed as a decision board, not a raw CSV view

## Public vs Private Boundary

This public repository should contain only reusable workflow code and documentation.

Public:

- `project-skill/`
- `scripts/`
- `examples/`
- `README.md`
- `PUBLISHING.md`
- `.gitignore`
- `LICENSE`

Private:

- browser profiles and login state
- raw scraped datasets
- generated reports
- personal resumes
- compensation records
- interview notes
- private Excel workbooks

## Repository Layout

```text
career-intelligence-copilot/
├── README.md
├── PUBLISHING.md
├── LICENSE
├── .gitignore
├── examples/
│   ├── incoming_jobs.example.json
│   └── power-trading-case.md
├── scripts/
│   ├── merge_master_dataset.py
│   ├── run_merge_master.cmd
│   └── update_weekly_job_market.example.py
└── project-skill/
    └── career-intelligence-copilot/
        ├── README.md
        ├── SKILL.md
        └── references/
            ├── file-map.md
            ├── master-dataset-merge.md
            ├── real-role-derived-guidance.md
            └── workbook-rules.md
```

## How To Use

Copy `project-skill/career-intelligence-copilot/` into a job-search workspace and adapt the file paths in `SKILL.md` to your local project.

Then ask Codex for work like:

```text
Use the career-intelligence-copilot skill to refresh this week's job-market dataset,
merge the normalized incoming rows, update the market report, and refresh company ranking.
```

```text
Based only on accepted postings in the current master dataset,
reverse-engineer which resume bullets and portfolio projects I should improve.
```

## Scripts

The repository includes a safe merge entrypoint:

```powershell
scripts\run_merge_master.cmd `
  --incoming-json examples\incoming_jobs.example.json `
  --master-csv output\jobs_master.csv `
  --master-json output\jobs_master.json `
  --summary-json tmp\merge_summary.json `
  --allow-initialize-empty-master
```

The browser-scraping layer is intentionally represented as an example scaffold. Real deployments should keep login state, raw data, and personalized analysis in a private workspace.

## Keywords

- Codex skill
- job market intelligence
- resume reverse-engineering
- company ranking
- browser automation
- Boss Zhipin
- Liepin
- power trading
