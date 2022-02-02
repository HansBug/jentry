import os
from typing import List, Iterator

import click

from ..script import load_entries_from_file, load_entries_from_project
from ...model import JavaEntry


def _click_load_entries(paths: List[str]) -> Iterator[JavaEntry]:
    for path in paths:
        if os.path.exists(path):
            if os.path.isfile(path):
                yield from load_entries_from_file(path)
            else:
                yield from load_entries_from_project(path)
        else:
            raise click.FileError(f'File not found - {repr(path)}.')  # pragma: no cover
