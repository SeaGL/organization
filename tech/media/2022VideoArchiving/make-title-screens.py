#!/usr/bin/env python3

from csv import DictReader
from math import ceil
from os import makedirs
from subprocess import run
from string import Template
from textwrap import wrap


# Workaround for https://gitlab.com/inkscape/inkscape/-/issues/2943
def issue2943(svg):
    return svg + ' ' * (len(bytes(svg, 'utf-8')) - len(svg))


makedirs('title-screens', exist_ok=True)

with open('title-screen.template.svg') as svg:
    template = Template(svg.read())

with open('seagl2022.ia.csv') as csv:
    for item in DictReader(csv):
        path = f"title-screens/{item['identifier']}.png"
        print(f"Render {path}")

        # Collect data
        is_keynote = 'Keynote' in item['description']
        title = item['title']
        presenters = list(filter(None, [
            item['creator[0]'],
            item['creator[1]'],
            item['creator[2]'],
            item['creator[3]']
        ]))

        # Format fields
        presenter = ', '.join(presenters[:-2] + [((len(presenters) != 2) * ',' + " and ").join(presenters[-2:])])
        if title == 'Keynote':
            title, presenter = presenter, ''
        target_width = max(28, min(38, round(len(title) / 2.5)))
        width = ceil(len(title) / ceil(len(title) / target_width)) + 4
        lines = wrap(title.upper(), width=width, break_long_words=False)
        wrapped_title = ''.join(f"<tspan x='0' y='{(1 + i - len(lines)) * 67}'>{l}</tspan>" for i, l in enumerate(lines))
        prefix = f"<tspan x='0' y='{(1 - len(lines)) * 67}'>KEYNOTE</tspan>" if is_keynote else ''

        # Render image
        svg = template.substitute(prefix=prefix, title=wrapped_title, presenter=presenter)
        run(('inkscape', '--pipe', '--export-filename', path), input=issue2943(svg), encoding='utf-8')
