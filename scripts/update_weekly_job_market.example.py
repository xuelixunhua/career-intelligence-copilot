from __future__ import annotations

"""
Public scaffold for a weekly job-market refresh.

Real browser scraping, login state, raw postings, resumes, compensation files,
and generated reports should live in a private workspace. This example shows
the control flow and filtering boundaries without embedding private data.
"""

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUN_DATE = dt.date.today().isoformat()
INCOMING_DIR = ROOT / "tmp" / "incoming"
MERGE_SCRIPT = ROOT / "scripts" / "merge_master_dataset.py"

ANONYMOUS_COMPANY_PATTERNS = [
    r"^某",
    r"^[北上广深杭天重成武苏南西郑].*某",
]
HEADHUNTER_KEYWORDS = ["猎头", "猎聘顾问", "招聘顾问"]
COMPANY_NAME_NOISE = {"急聘", "统招本科", "本科", "硕士", "博士", "大专", "学历不限", "经验不限"}


def normalize_space(text: str) -> str:
    text = text.replace("\u3000", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n{2,}", "\n", text).strip()


def looks_like_salary(text: str) -> bool:
    value = normalize_space(text).lower()
    return bool(re.fullmatch(r"\d+(?:\.\d+)?-\d+(?:\.\d+)?k(?:·\d+薪)?", value))


def is_company_name_noise(name: str) -> bool:
    text = normalize_space(name)
    return not text or text in COMPANY_NAME_NOISE or looks_like_salary(text)


def classify_record(record: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    company_name = normalize_space(str(record.get("company_name", "") or ""))
    recruiter_text = normalize_space(
        f"{record.get('recruiter_name', '')} {record.get('recruiter_title', '')}"
    )
    source_url = str(record.get("source_url", "") or "")

    if any(re.search(pattern, company_name) for pattern in ANONYMOUS_COMPANY_PATTERNS):
        reasons.append("anonymous company")
    if is_company_name_noise(company_name):
        reasons.append("missing or malformed company name")
    if any(keyword in recruiter_text for keyword in HEADHUNTER_KEYWORDS):
        reasons.append("headhunter role")
    if record.get("source_platform") == "liepin" and "/a/" in source_url:
        reasons.append("anonymous Liepin recommendation")

    return list(dict.fromkeys(reasons))


def apply_acceptance_filters(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    kept: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    for record in records:
        reasons = classify_record(record)
        record["accepted"] = not reasons
        record["filter_reasons"] = "；".join(reasons)
        (kept if record["accepted"] else dropped).append(record)
    return kept, dropped


def fetch_current_listings() -> list[dict[str, Any]]:
    """
    Replace this with project-specific browser automation.

    The scraper should return normalized dictionaries with the incoming fields
    documented in project-skill/career-intelligence-copilot/references/master-dataset-merge.md.
    """
    raise NotImplementedError("Implement private browser scraping in your own workspace.")


def write_incoming(records: list[dict[str, Any]]) -> Path:
    INCOMING_DIR.mkdir(parents=True, exist_ok=True)
    path = INCOMING_DIR / f"jobs_{RUN_DATE}.json"
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def merge_incoming(incoming_json: Path, expected_existing_min: int | None = None) -> None:
    cmd = [
        sys.executable,
        str(MERGE_SCRIPT),
        "--incoming-json",
        str(incoming_json),
        "--summary-json",
        str(INCOMING_DIR / f"merge_summary_{RUN_DATE}.json"),
    ]
    if expected_existing_min is None:
        cmd.append("--allow-initialize-empty-master")
    else:
        cmd.extend(["--expected-existing-min", str(expected_existing_min)])
    subprocess.run(cmd, check=True)


def main() -> None:
    records = fetch_current_listings()
    kept, dropped = apply_acceptance_filters(records)
    incoming_json = write_incoming(kept)
    merge_incoming(incoming_json)
    print(json.dumps({"incoming": len(kept), "dropped": len(dropped)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
