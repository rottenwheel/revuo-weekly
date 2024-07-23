#!/usr/bin/env python3

import subprocess
import pathlib
import argparse
import datetime
import tempfile
import tomllib


def create_issue(issue_number):
    subprocess.run(["hugo", "new", f"weekly/issue-{issue_number}/_index.md"])


def create_issue_image(site_title, issue_number, period_start, period_end):
    with open("assets/img/cover-template.svg") as f:
        cover_template = f.read()

    cover_template = cover_template.replace("__SITE__", site_title)
    cover_template = cover_template.replace("__ISSUE__", issue_number)
    cover_template = cover_template.replace(
        "__DATE__", f"{period_start} - {period_end}"
    )

    with tempfile.TemporaryDirectory() as tempdir:
        cover_path = pathlib.Path(tempdir) / "cover.svg"
        with open(cover_path, "w") as f:
            f.write(cover_template)

        subprocess.run(
            [
                "inkscape",
                str(cover_path),
                "-e",
                f"content/weekly/issue-{issue_number}/cover.png",
            ]
        )


def get_latest_issue():
    issues = list(pathlib.Path("content/weekly").iterdir())
    latest_issue = max(issues, key=lambda x: int(x.name.split("-")[1]))
    return latest_issue.name.split("-")[1]


if __name__ == "__main__":
    with open("hugo.toml", "rb") as f:
        hugo_config = tomllib.load(f)

    parser = argparse.ArgumentParser(description="Create a new issue")
    parser.add_argument("--issue", type=int, help="Issue number")
    args = parser.parse_args()

    if args.issue:
        new_issue = args.issue
    else:
        latest_issue = get_latest_issue()
        new_issue = int(latest_issue) + 1

    period_start = datetime.datetime.now().strftime("%Y-%m-%d")
    period_end = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime(
        "%Y-%m-%d"
    )

    create_issue(new_issue)
