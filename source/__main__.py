"""
"""
import parser

"""
argument_parser = parser.Parser()
argument_parser.parse_arguments()

print(argument_parser.arguments)
print(argument_parser.unknown)
"""

import os
import sys
import shutil
from pathlib import Path

def iterdirs(directories):
    for directory in directories:
        for item in directory.iterdir():
            yield item


argument_parser = parser.Parser()
argument_parser.parse_arguments()

print(argument_parser.arguments)
print(argument_parser.arguments["sources"])


destination = Path(argument_parser.arguments["destination"])

destination.mkdir(exist_ok=True)
for index, item in enumerate(iterdirs([Path(source) for source in argument_parser.arguments["sources"]])):
    p = Path(item)
    s = p.name
    #p.rename(str(destination) + str(index) + "__" + s)
    shutil.copy2(str(p), str(destination) + "/" + str(index) + "jimmy")


"""
os.mkdir("dir2")
for index, p in enumerate(Path("dir").iterdir()):
    p = Path(p)
    s = p.name
    p.rename("dir2/100_" + s)
"""

"""
input_dir = Path(sys.argv[1])

def get_all_filetypes(directory):
    filetypes = set()
    add_filetypes(directory, filetypes)

    return filetypes


def add_filetypes(directory, filetypes):
    for item in directory.iterdir():
        if item.is_dir():
            add_filetypes(item, filetypes)
        else:
            filetypes.add(item.suffix)


if len(sys.argv) < 2:
    print("wrong args")
    exit(1)

if not input_dir.exists():
    print("doesnt exist")
    exit(1)

if not input_dir.is_dir():
    print("not dir")
    exit(1)

filetypes = get_all_filetypes(input_dir)
print(filetypes)
"""
