#!/usr/bin/env python3

from argparse import ArgumentParser
from csv import DictWriter
from datetime import datetime
from itertools import chain
from markdown_it import MarkdownIt  # https://pypi.org/project/markdown-it-py/
from pathlib import Path
import re
from sys import stdout
from yaml import safe_load  # https://pypi.org/project/PyYAML/

markdown_it = MarkdownIt("commonmark")
markdown_it.add_render_rule("softbreak", lambda s, t, i, o, e: " ")  # markdown-it/markdown-it#611

arg_parser = ArgumentParser()
arg_parser.add_argument("archive_sessions_dir", type=Path)
arg_parser.add_argument("uploads_dir", type=Path)
args = arg_parser.parse_args()


def to_item(session_path):
    _, yaml, description = re.split("^---$", session_path.read_text(), 2, re.M)
    session = safe_load(yaml)

    identifier = session.get("resources", {}).get("internet_archive_identifier")
    if identifier is None:
        return

    beginning = datetime.fromisoformat(session["beginning"])

    return {
        "collection": "seagl",
        "date": beginning.date().isoformat(),
        "description": markdown_it.render(description),
        "file": args.uploads_dir / f"{identifier}.mp4",
        "identifier": identifier,
        "language": "English",
        "licenseurl": "https://creativecommons.org/licenses/by-sa/4.0/",
        "mediatype": "movies",
        "publisher": "Seattle GNU/Linux Conference",
        "title": session["title"],
        "year": beginning.year,
    } | {f"creator[{i}]": p["name"] for i, p in enumerate(session["presenters"])}


items = sorted(
    filter(None, map(to_item, args.archive_sessions_dir.iterdir())),
    key=lambda i: i["identifier"],
)
fields = sorted(set(chain.from_iterable([i.keys() for i in items])))

csv = DictWriter(stdout, fieldnames=fields)
csv.writeheader()
[csv.writerow(i) for i in items]
