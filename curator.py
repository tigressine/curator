"""
"""
import shutil
import pathlib
import argparse
import datetime


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
DEFAULT_TITLE = "New Album"
TITLE_FORMAT = "{year}-{month} {title}"
ITEM_FORMAT = "{initials}_{sequence}{extension}"


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
        self.add_argument("--year", default=datetime.datetime.now().year)
        self.add_argument("--month", default=datetime.datetime.now().month)

    def __parse_arguments(self):
        """Parse known arguments and save them."""
        self.arguments, self.unknown = self.parse_known_args()
        self.arguments = vars(self.arguments)

    def __validate_arguments(self):
        """"""
        # handle making video

        self.arguments["destination"] = pathlib.Path(self.arguments["destination"])
        self.arguments["sources"] = set(
            map(
                lambda source: pathlib.Path(source),
                self.arguments["sources"],
            ),
        )

        self.arguments["month"] = int(self.arguments["month"])
        self.arguments["year"] = int(self.arguments["year"])

        # ensure that dest and src exist and are accessible
        # sanitize title

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


# Main entry point of the script.
parser = Parser()

image_index = 0
video_index = 0
destination = parser.arguments["destination"] / TITLE_FORMAT.format(
    year=parser.arguments["year"],
    month=parser.arguments["month"],
    title=parser.arguments["title"],
)
for source_directory in parser.arguments["sources"]:
    for item in source_directory.iterdir():
        lowercase_suffix = item.suffix.lower()
        if lowercase_suffix in KNOWN_IMAGE_TYPES:
            shutil.copy2(
                item,
                destination / ITEM_FORMAT.format(
                    initials=parser.arguments["initials"],
                    sequence=image_index,
                    extension=lowercase_suffix,
                ),
            )
            image_index += 1
        elif lowercase_suffix in KNOWN_VIDEO_TYPES:
            shutil.copy2(
                item,
                destination / "videos" / ITEM_FORMAT.format(
                    initials=parser.arguments["initials"],
                    sequence=video_index,
                    extension=lowercase_suffix,
                ),
            )
            video_index += 1
        else:
            print("here")
            print("unknown file type")
            # handle weird file types
