""""""
import constants

import pathlib
import utilities

parser = utilities.Parser()
parser.parse_arguments()

print(parser.arguments)

index = 0
for source_directory in parser.arguments["sources"]:
    for item in source_directory.iterdir():
        utilities.copy_file(
            item,
            parser.arguments["destination"],
            constants.DEFAULT_ITEM_FORMAT,
            dict(
                initials="TGS",
                sequence=index,
                extension="txt",
            ),
        )
        index += 1
