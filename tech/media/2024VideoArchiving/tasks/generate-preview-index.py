#!/usr/bin/env python3

from argparse import ArgumentParser
from csv import DictReader
from html import escape as text_to_html
from pathlib import Path
import re
from string import Template
from urllib.parse import quote as text_to_url

creator_key_pattern = re.compile(r"^creator\[\d+\]$")

arg_parser = ArgumentParser()
arg_parser.add_argument("uploads_dir", type=Path)
arg_parser.add_argument("spreadsheet_path", type=Path)
arg_parser.add_argument("index_path", type=Path)
args = arg_parser.parse_args()


def creator_to_html(name):
    query = f'creator:"{name}"'
    url = f"https://archive.org/search.php?query={text_to_url(query)}"

    return f'<a href="{text_to_html_attribute(url)}">{text_to_html(name)}</a>'


def session_to_html(session):
    video_path = Path(session["file"]).relative_to(args.uploads_dir)

    collection_url = f'https://archive.org/details/{text_to_url(session["collection"])}'
    creators_html = ", ".join(
        [creator_to_html(session[k]) for k in creator_keys if session[k]]
    )
    session_url = f'#{text_to_url(session["identifier"])}'
    poster_url = f'./{text_to_url(str(video_path.with_suffix(".jpg")))}'
    video_url = f'./{text_to_url(str(video_path.with_suffix(".preview.mp4")))}'

    return f"""
        <article id="{text_to_html_attribute(session["identifier"])}">
            <video controls preload="none" poster="{text_to_html_attribute(poster_url)}" src="{text_to_html_attribute(video_url)}" height="360" width="640"></video>
            <h2><a href="{text_to_html_attribute(session_url)}">{text_to_html(session["title"])}</a></h2>
            <p class="byline">by {creators_html}</p>
            <dl>
                <dt>URL</dt><dd><code>https://archive.org/details/{text_to_html(session["identifier"])}</code></dd>
                <dt>Date</dt><dd>{text_to_html(session["date"])}</dd>
                <dt>Language</dt><dd>{text_to_html(session["language"])}</dd>
                <dt>License</dt><dd><a href="{text_to_html_attribute(session["licenseurl"])}">{text_to_html(session["licenseurl"])}</a></dd>
                <dt>Publisher</dt><dd>{text_to_html(session["publisher"])}</dd>
                <dt>Collection</dt><dd><a href="{text_to_html_attribute(collection_url)}">{text_to_html(session["collection"])}</a></dd>
            </dl>
            {session["description"]}
        </article>
    """


def text_to_html_attribute(text):
    return text_to_html(text, True)


with args.spreadsheet_path.open() as f:
    reader = DictReader(f)

    creator_keys = [k for k in reader.fieldnames or [] if creator_key_pattern.match(k)]
    sessions = list(reader)

with open("resources/index.html.template") as f:
    template = Template(f.read())

args.index_path.parent.mkdir(parents=True, exist_ok=True)
args.index_path.write_text(
    template.substitute(sessions="\n".join(map(session_to_html, sessions)))
)
