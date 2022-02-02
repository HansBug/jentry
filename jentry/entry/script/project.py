import os
from typing import Iterator

from .file import load_entries_from_file
from ...model import JavaEntry


def load_entries_from_project(project_dir: str) -> Iterator[JavaEntry]:
    for path, dirs, files in os.walk(project_dir, followlinks=True):
        for f in files:
            if f.endswith('.java'):
                yield from load_entries_from_file(os.path.join(path, f))
