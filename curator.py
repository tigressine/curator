"""
"""
import shutil
import pathlib
import argparse
import datetime


class Parser(argparse.ArgumentParser):
    """Class that handles command line arguments."""

    def __init__(self, *args, **kwargs):
        """Initialize super and add some arguments."""
        super().__init__(*args, add_help=False, **kwargs)
        self.__add_arguments()
        self.__parse_arguments()
        self.__validate_arguments()
        if self.arguments["initials"] is None:
            self.__determine_initials()
        

    def __add_arguments(self):
        """"""
        self.add_argument("destination")
        self.add_argument("sources", nargs="+")
        self.add_argument("--initials", default=None)
        self.add_argument("--title", default=DEFAULT_TITLE)
        self.add_argument("--item-format", default=DEFAULT_ITEM_FORMAT)
        self.add_argument("--title-format", default=DEFAULT_TITLE_FORMAT)
        self.add_argument("--transfer-method", default=DEFAULT_TRANSFER_METHOD)
        self.add_argument("--year", default=datetime.datetime.now().year)
        self.add_argument("--month", default=datetime.datetime.now().month)
        self.add_argument(
            "--unknown-filetype-strategy",
            default=DEFAULT_UNKNOWN_FILETYPE_STRATEGY,
        )

    def __parse_arguments(self):
        """Parse known arguments and save them."""
        self.arguments, self.unknown = self.parse_known_args()
        self.arguments = vars(self.arguments)

    def __validate_arguments(self):
        """"""
        # handle making video
        # make dest pathlib
        # make src pathlib
        self.arguments["destination"] = pathlib.Path(self.arguments["destination"])
        self.arguments["sources"] = set(
            map(
                lambda source: pathlib.Path(source),
                self.arguments["sources"],
            ),
        )

        # make year and month int
        self.arguments["month"] = int(self.arguments["month"])
        self.arguments["year"] = int(self.arguments["year"])

        # ensure that strategy, transfer are valid

        # set strategy
        method = self.arguments["transfer_method"]
        if method in TRANSFER_METHODS.keys():
            self.arguments["transfer_method"] = TRANSFER_METHODS[method]
        else:
            pass #

        # ensure that dest and src exist and are accessible
        # sanitize title and formats

    def __determine_initials(self):
        """"""
        self.arguments["initials"] = "".join(
            filter(
                lambda character: character.isupper(),
                self.arguments["title"],
            ),
        )

    def error(self, message):
        """If any parsing error occurs, help the user."""
        pass


def copy_file(item, destination, target_format, target_format_arguments):
    """"""
    target = pathlib.Path(destination) / target_format.format(**target_format_arguments)
    shutil.copy2(str(item), str(target))


def move_file(item, destination, target_format, target_format_arguments):
    """"""
    target = pathlib.Path(destination) / target_format.format(**target_format_arguments)
    pathlib.Path(item).rename(target)


# Constants and defaults for this script.
KNOWN_IMAGE_TYPES = {
    ".bmp",
    ".png",
    ".jpg",
    ".jpeg",
    ".tiff",
}
KNOWN_VIDEO_TYPES = {
    ".mp4",
    ".avi",
    ".mov",
    ".wmv",
}
DEFAULT_TITLE = "album"
DEFAULT_TITLE_FORMAT = "{year}-{month}_{title}"
DEFAULT_ITEM_FORMAT = "{initials}_{sequence}{extension}"
DEFAULT_TRANSFER_METHOD = "copy"
TRANSFER_METHODS = {
    "copy" : copy_file,
    "move" : move_file,
}
DEFAULT_UNKNOWN_FILETYPE_STRATEGY = "ignore"
UNKNOWN_FILETYPE_STRATEGIES = {
    "copy",
    "move",
    "ignore",
}


# Main entry point of the script.
parser = Parser()
print(parser.arguments)

image_index = 0
video_index = 0
for source_directory in parser.arguments["sources"]:
    for item in source_directory.iterdir():
        lowercase_suffix = item.suffix.lower()
        print(lowercase_suffix)
        if lowercase_suffix in KNOWN_IMAGE_TYPES:
            parser.arguments["transfer_method"](
                item,
                parser.arguments["destination"],
                DEFAULT_ITEM_FORMAT,
                dict(
                    initials=parser.arguments["initials"],
                    sequence=image_index,
                    extension=lowercase_suffix,
                ),
            )
            image_index += 1
        elif lowercase_suffix in KNOWN_VIDEO_TYPES:
            parser.arguments["transfer_method"](
                item,
                parser.arguments["destination"] / "videos",
                DEFAULT_ITEM_FORMAT,
                dict(
                    initials=parser.arguments["initials"],
                    sequence=video_index,
                    extension=lowercase_suffix,
                ),
            )
            video_index += 1
        else:
            print("here")
            # handle weird file types
            pass
