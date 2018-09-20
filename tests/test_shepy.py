from pathlib import Path
from shepy import *
import pytest
import sys



def test_pwd():
    assert pwd() == Path(sys.argv[0]).parent

def test_joinpath():
    with pytest.raises(SystemExit):
        joinpath()

    assert joinpath("/") == Path("/").resolve()

    assert joinpath("/", "folder1") == Path("/folder1").resolve()

    assert joinpath("/", "folder1", "folder2") == \
        Path("/folder1/folder2").resolve()

    assert joinpath("/", "", "folder1", "folder2") == \
        Path("/folder1/folder2").resolve()

def test_mkdir():
    with pytest.raises(TypeError):
        #pylint: disable=E1120
        mkdir()