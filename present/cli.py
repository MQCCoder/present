# -*- coding: utf-8 -*-

import os
import click

from .slideshow import Slideshow
from .markdown import Markdown


@click.command()
@click.argument("filename")
def cli(filename):
    """present: A terminal-based presentation tool."""

    markdown = Markdown()

    with open(filename, "r") as f:
        slides = markdown.parse(f.read())

    show = Slideshow(slides)
    try:
        show.play()
    except KeyboardInterrupt:
        pass
    finally:
        # TODO: asciimatics leaves terminal in abnormal state
        # temp fix till underlying bug is found and fixed
        if os.name == "posix":
            os.system("reset")
