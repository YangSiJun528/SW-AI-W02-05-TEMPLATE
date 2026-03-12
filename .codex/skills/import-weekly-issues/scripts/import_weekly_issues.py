#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


LABEL_COLORS = {
    "category_common": "d4c5f9",
    "category_basic": "bfd4f2",
    "category_problem_solving": "f9d0c4",
    "category_extra": "c2e0c6",
    "difficulty_low": "0e8a16",
    "difficulty_medium": "fbca04",
    "difficulty_high": "d93f0b",
}

DIFFICULTY_LABELS = {
    "난이도하": "difficulty_low",
    "난이도중": "difficulty_medium",
    "난이도상": "difficulty_high",
}

SUFFIX_PATTERNS = (
    re.compile(r"(브론즈|실버|골드|플래)\d+$"),
    re.compile(r"백준(브론즈|실버|골드|플래)\d+$"),
)


@dataclass
class IssueDraft:
    title: str
    body: str
    labels: list[str]
    category: str
    difficulty: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create GitHub issues from weekN CSV files with labels."
    )
    parser.add_argument("week", help="Week folder name such as week2")
    parser.add_argument("--repo", help="GitHub repo in owner/name format")
    parser.add_argument("--owner", help="GitHub project owner")
    parser.add_argument("--project-number", type=int, default=1)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually create labels/issues and add items to the project",
    )
    parser.add_argument(
        "--skip-project-add",
        action="store_true",
        help="Create issues only, without adding them to the project",
    )
    return parser.parse_args()


def run(
    args: list[str],
    *,
    cwd: Path,
    capture_output: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=str(cwd),
        check=True,
        text=True,
        capture_output=capture_output,
    )


def normalize_key(value: str) -> str:
    collapsed = re.sub(r"[^0-9A-Za-z가-힣]+", "", value).casefold()
    return collapsed


def clean_problem_stem(stem: str) -> str:
    value = stem
    for token in ("_2차", "_답"):
        value = value.replace(token, "")
    value = value.replace("_", "")
    value = value.replace("백준", "")
    for pattern in SUFFIX_PATTERNS:
        value = pattern.sub("", value)
    return value


def infer_repo_from_git(root: Path) -> str:
    result = run(["git", "remote", "get-url", "origin"], cwd=root)
    remote = result.stdout.strip()
    match = re.search(r"github\.com[:/](?P<repo>[^/]+/[^/.]+)(?:\.git)?$", remote)
    if not match:
        raise SystemExit(f"Could not infer repo from origin remote: {remote}")
    return match.group("repo")


def infer_owner(repo: str) -> str:
    return repo.split("/", 1)[0]


def build_body(content: str) -> str:
    content = content.strip()
    if not content:
        return ""
    if re.match(r"https?://", content):
        return f"Reference: {content}"
    return content


def parse_category(title: str) -> tuple[str, str]:
    if title.startswith("공통 - "):
        return "category_common", title.removeprefix("공통 - ").strip()
    if title.startswith("basic - "):
        return "category_basic", title.removeprefix("basic - ").strip()
    if title.startswith("Extra - "):
        return "category_extra", title.removeprefix("Extra - ").strip()
    return "category_problem_solving", title.strip()


def collect_difficulty_map(week_dir: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    problem_dir = week_dir / "problem-solving"
    if not problem_dir.exists():
        return mapping

    for path in sorted(problem_dir.glob("*.py")):
        parts = path.stem.split("_")
        if not parts:
            continue
        prefix = parts[0]
        if prefix not in DIFFICULTY_LABELS:
            continue
        difficulty_label = DIFFICULTY_LABELS[prefix]
        if len(parts) < 3:
            continue
        problem_name = clean_problem_stem("_".join(parts[2:]))
        key = normalize_key(problem_name)
        if key and key not in mapping:
            mapping[key] = difficulty_label
    return mapping


def load_issue_drafts(week_dir: Path) -> list[IssueDraft]:
    csv_path = week_dir / f"{week_dir.name}_issues_complete.csv"
    if not csv_path.exists():
        raise SystemExit(f"CSV file not found: {csv_path}")

    week_label = week_dir.name.replace("week", "week_")
    difficulty_map = collect_difficulty_map(week_dir)
    drafts: list[IssueDraft] = []

    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            raw_title = (row.get("title") or "").strip()
            raw_content = row.get("content") or ""
            if not raw_title:
                continue

            category, stripped_title = parse_category(raw_title)
            labels = [week_label, category]
            difficulty = None

            if category == "category_problem_solving":
                topic_and_name = stripped_title.split(" - ", 1)
                problem_name = topic_and_name[-1].strip()
                difficulty = difficulty_map.get(normalize_key(problem_name))
                if difficulty:
                    labels.append(difficulty)

            drafts.append(
                IssueDraft(
                    title=raw_title,
                    body=build_body(raw_content),
                    labels=labels,
                    category=category,
                    difficulty=difficulty,
                )
            )

    return drafts


def ensure_labels_exist(root: Path, labels: Iterable[str], repo: str) -> None:
    repo_view = run(
        ["gh", "repo", "view", repo, "--json", "labels"],
        cwd=root,
    )
    payload = json.loads(repo_view.stdout)
    existing = {item["name"] for item in payload.get("labels", [])}

    for label in sorted(set(labels)):
        if label in existing:
            continue
        color = LABEL_COLORS.get(label, "ededed")
        run(
            [
                "gh",
                "label",
                "create",
                label,
                "--repo",
                repo,
                "--color",
                color,
            ],
            cwd=root,
        )


def create_issue(root: Path, repo: str, draft: IssueDraft) -> str:
    cmd = [
        "gh",
        "issue",
        "create",
        "--repo",
        repo,
        "--title",
        draft.title,
    ]
    if draft.body:
        cmd.extend(["--body", draft.body])
    else:
        cmd.extend(["--body", ""])
    if draft.labels:
        cmd.extend(["--label", ",".join(draft.labels)])
    result = run(cmd, cwd=root)
    return result.stdout.strip()


def add_issue_to_project(root: Path, owner: str, project_number: int, issue_url: str) -> None:
    run(
        [
            "gh",
            "project",
            "item-add",
            str(project_number),
            "--owner",
            owner,
            "--url",
            issue_url,
        ],
        cwd=root,
    )


def print_summary(
    drafts: list[IssueDraft],
    *,
    week: str,
    repo: str,
    owner: str,
    project_number: int,
    skip_project_add: bool,
) -> None:
    category_counts = Counter(draft.category for draft in drafts)
    difficulty_counts = Counter(
        draft.difficulty for draft in drafts if draft.difficulty is not None
    )
    label_counts = Counter(label for draft in drafts for label in draft.labels)

    print(f"Week: {week}")
    print(f"Repo: {repo}")
    print(f"Project owner: {owner}")
    print(f"Project number: {project_number}")
    print(f"Project add: {'no' if skip_project_add else 'yes'}")
    print(f"Total issues: {len(drafts)}")
    print()
    print("Category counts:")
    for label, count in sorted(category_counts.items()):
        print(f"  - {label}: {count}")
    print("Difficulty counts:")
    if difficulty_counts:
        for label, count in sorted(difficulty_counts.items()):
            print(f"  - {label}: {count}")
    else:
        print("  - none")
    print("Label counts:")
    for label, count in sorted(label_counts.items()):
        print(f"  - {label}: {count}")
    print()
    print("Preview:")
    for draft in drafts[:10]:
        print(f"  - {draft.title} :: {', '.join(draft.labels)}")
    remaining = len(drafts) - min(10, len(drafts))
    if remaining > 0:
        print(f"  ... {remaining} more")


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    root = script_path.parents[4]
    week_dir = root / args.week
    if not week_dir.exists():
        raise SystemExit(f"Week directory not found: {week_dir}")

    repo = args.repo or infer_repo_from_git(root)
    owner = args.owner or infer_owner(repo)
    drafts = load_issue_drafts(week_dir)

    if not drafts:
        raise SystemExit(f"No issues found in {week_dir}")

    print_summary(
        drafts,
        week=args.week,
        repo=repo,
        owner=owner,
        project_number=args.project_number,
        skip_project_add=args.skip_project_add,
    )

    if not args.execute:
        print()
        print("Dry-run only. Re-run with --execute after user approval.")
        return 0

    all_labels = {label for draft in drafts for label in draft.labels}
    ensure_labels_exist(root, all_labels, repo)

    failures: list[str] = []
    created = 0
    added = 0

    for draft in drafts:
        try:
            issue_url = create_issue(root, repo, draft)
            created += 1
            if not args.skip_project_add:
                add_issue_to_project(root, owner, args.project_number, issue_url)
                added += 1
        except subprocess.CalledProcessError as exc:
            failures.append(
                f"{draft.title}: {exc.stderr.strip() or exc.stdout.strip() or exc}"
            )

    print()
    print(f"Created issues: {created}")
    print(f"Project additions: {added}")
    if failures:
        print("Failures:")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
