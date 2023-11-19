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


def to_item(session_path):
    _, yaml, description = re.split("^---$", session_path.read_text(), 2, re.M)
    session = safe_load(yaml)

    identifier = session["resources"]["internet_archive_identifier"]
    beginning = datetime.fromisoformat(session["beginning"])

    return {
        "collection": "seagl",
        "date": beginning.date().isoformat(),
        "description": markdown_it.render(description),
        "file": f"{identifier}.mp4",
        "identifier": identifier,
        "language": "English",
        "licenseurl": "https://creativecommons.org/licenses/by-sa/4.0/",
        "mediatype": "movies",
        "publisher": "Seattle GNU/Linux Conference",
        "title": session["title"],
        "year": beginning.year,
    } | {f"creator[{i}]": p["name"] for i, p in enumerate(session["presenters"])}


arg_parser = ArgumentParser()
arg_parser.add_argument("sessions_dir", type=Path)
args = arg_parser.parse_args()

items = sorted(map(to_item, args.sessions_dir.iterdir()), key=lambda i: i["identifier"])
fields = sorted(set(chain.from_iterable([i.keys() for i in items])))

csv = DictWriter(stdout, fieldnames=fields)
csv.writeheader()
[csv.writerow(i) for i in items]
