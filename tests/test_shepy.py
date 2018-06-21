from pathlib import Path
from shepy import *

def test_joinpath():
    assert joinpath("/") == Path("/").resolve()
    assert joinpath("/", "folder1") == Path("/folder1").resolve()
    assert joinpath("/", "folder1", "folder2") == \
        Path("/folder1/folder2").resolve()