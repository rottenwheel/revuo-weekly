#!/usr/bin/env python3

import subprocess
import pathlib
import argparse
import datetime
import tempfile
import tomllib
from PIL import Image

def get_period_string(
    start: datetime.datetime,
    end: datetime.datetime,
    year: bool = False,
) -> str:
    """Get a string representation of the period

    Args:
        start (datetime.datetime): The start of the period
        end (datetime.datetime): The end of the period
        year (bool, optional): Include the year in the string. Defaults to False.

    Returns:
        str: The period string
    """
    if period_start.year == period_end.year:
        if period_start.month == period_end.month:
            period_string = (
                f"{period_start.strftime('%B %-d')} - {period_end.strftime('%-d')}"
            )
        else:
            period_string = (
                f"{period_start.strftime('%B %-d')} - {period_end.strftime('%B %-d')}"
            )

        if year:
            period_string += f", {period_start.year}"

    else:
        period_string = (
            f"{period_start.strftime('%B %-d, %Y')} - {period_end.strftime('%B %-d, %Y')}"
        )

    return period_string


def create_issue(
    issue_number: int, period_start: datetime.datetime, period_end: datetime.datetime
) -> None:
    """Create a new issue

    Args:
        issue_number (int): The issue number
        period_start (datetime.datetime): The start of the period
        period_end (datetime.datetime): The end of the period

    Raises:
        subprocess.CalledProcessError: If the Hugo command fails
        IOError: If any of the Python file operations fail
    """
	# Use the Hugo CLI to create a new issue
    subprocess.run(
        ["hugo", "new", f"weekly/issue-{issue_number}/_index.md"], check=True
    )

	# Read the content of the new file
    with open(f"content/weekly/issue-{issue_number}/_index.md", "r") as f:
        content = f.read()

    # Get line that starts with "title" and replace it with the new title
    lines = content.split("\n")

    period_string = get_period_string(period_start, period_end, True)
    meeting_placeholder = f"{period_start.strftime("%B")} [day], {period_start.year}"
    data_placeholder = period_end.strftime("%B %-d, %Y")
    tabledata_placeholder = period_end.strftime("%m/%d/%y")

    for i, line in enumerate(lines):
        if line.startswith("title:"):
            lines[i] = f'title: "Issue {issue_number}: {period_string}"'
        elif line.startswith("{{% event"): # replace date in event shortcode
            lines[i] = line.replace("July 1, 2024", meeting_placeholder)
        elif 'date="January 1, 2024"' in line: #replace date in bc_stats shortcode
            lines[i] = line.replace("January 1, 2024", data_placeholder)
        elif 'date="June 6, 2024"' in line: #replace date in price_performance shortcode
            lines[i] = line.replace("June 6, 2024", data_placeholder)
        elif 'table_date="06/13/24"' in line: #replace table_date in price_performance shortcode
            lines[i] = line.replace("06/13/24", tabledata_placeholder)

    content = "\n".join(lines)

	# Overwrite the file with the new content
    with open(f"content/weekly/issue-{issue_number}/_index.md", "w") as f:
        f.write(content)


def create_issue_image(
    site_title: str,
    issue_number: int,
    period_start: datetime.datetime,
    period_end: datetime.datetime,
) -> None:
    """Create a cover image for the issue

    Args:
        site_title (str): The title of the site
        issue_number (int): The issue number
        period_start (datetime.datetime): The start of the period
        period_end (datetime.datetime): The end of the period

    Raises:
        FileNotFoundError: If the cover template is not found
        IOError: If any of the file operations fail
    """
    with open("assets/img/cover-template.svg") as f:
        cover_template = f.read()

    period_string = get_period_string(period_start, period_end)

    cover_template = cover_template.replace("__SITE__", site_title)
    cover_template = cover_template.replace("__TITLE__", f"ISSUE {issue_number}")
    cover_template = cover_template.replace("__DATE__", period_string)

    with tempfile.TemporaryDirectory() as tempdir:
        cover_path = pathlib.Path(tempdir) / "cover.svg"
        with open(cover_path, "w") as f:
            f.write(cover_template)

        subprocess.run(
            [
                "inkscape",
                str(cover_path),
                "--export-filename",
                f"content/weekly/issue-{issue_number}/cover.png",
            ]
        )

        image = Image.open(f"content/weekly/issue-{issue_number}/cover.png")
        image = image.convert("RGB").quantize(colors=256)
        image.save(f"content/weekly/issue-{issue_number}/cover.png", "PNG", compress_level=9)

def get_latest_issue() -> int:
    """Get the latest issue number from the weekly directory

    Returns:
        int: The latest issue number
    """
    issues = list(pathlib.Path("content/weekly").iterdir())
    latest_issue = max(issues, key=lambda x: int(x.name.split("-")[1]))
    return int(latest_issue.name.split("-")[1])


if __name__ == "__main__":
    with open("hugo.toml", "rb") as f:
        hugo_config = tomllib.load(f)

    parser = argparse.ArgumentParser(description="Create a new issue")
    parser.add_argument("--issue", type=int, help="Issue number")
    parser.add_argument("--period-start", type=str, help="Period start")
    parser.add_argument("--period-end", type=str, help="Period end")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet mode")
    args = parser.parse_args()

    if not (args.period_start and args.period_end):
        if not args.quiet:
            # Query the user for the period start and end
            today = datetime.datetime.now().strftime("%Y-%m-%d")

            period_start_str = input(f"Period start [{today}]: ") or today
            period_start = datetime.datetime.strptime(period_start_str, "%Y-%m-%d")

            seven_days = (period_start + datetime.timedelta(days=7)).strftime(
                "%Y-%m-%d"
            )

            period_end_str = input(f"Period end [{seven_days}]: ") or seven_days
            period_end = datetime.datetime.strptime(period_end_str, "%Y-%m-%d")

        else:
            # Assume the period is the next 7 days - # TODO: Check if this is correct
            period_start = datetime.datetime.now()
            period_end = datetime.datetime.now() + datetime.timedelta(days=7)

    if args.issue:
        new_issue = args.issue
    else:
        latest_issue = get_latest_issue()
        new_issue = int(latest_issue) + 1

    create_issue(new_issue, period_start, period_end)
    create_issue_image("Revuo Weekly", new_issue, period_start, period_end)
