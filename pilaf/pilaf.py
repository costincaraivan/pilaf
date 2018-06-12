from pathlib import Path
import shutil
import sys
from zipfile import ZipFile

def pwd():
    return Path(sys.argv[0]).parent

def joinpath(path1, path2):
    return Path(path1).joinpath(path2).resolve()

def mkdir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def rmdir(path):
    Path(path).rmdir()

def rm(path):
    shutil.rmtree(path)

def archive(*args):
    if len(args) == 0:
        print("No arguments given for zip.")
        sys.exit(1)
    if len(args) == 1:
        print(f"""Just the name of the archive given as parameter, {args[0]}
            archiving the current folder: {pwd()}.""")
    with(ZipFile("ansible.zip", "w")) as zip_archive:
        pass