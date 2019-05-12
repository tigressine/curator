"""Curate images and videos with this simple script!

Written by Tiger Sachse.
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
DEFAULT_TITLE = "Album"
DEFAULT_CLIPS_DIRECTORY = "Clips"
TITLE_FORMAT = "{year}-{month} {title}"
ITEM_FORMAT = "{initials}_{sequence}{extension}"


class Parser(argparse.ArgumentParser):
    """This class parses and sanitizes command line arguments."""

    def __init__(self, *args, **kwargs):
        """Initialize super and add some arguments."""
        super().__init__(*args, add_help=False, **kwargs)
        self.__add_arguments()

    def parse_arguments(self):
        """Parse the command line arguments."""
        self.__parse_arguments()
        self.__sanitize_arguments()
        if self.arguments["initials"] is None:
            self.__determine_initials()
        
    def error(self, message):
        """If any parsing error occurs, tell the user."""
        print("An error occurred:", message)

    def __add_arguments(self):
        """Add a handful of arguments to this script."""
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

    def __sanitize_arguments(self):
        """Transform some arguments into more useful forms."""
        self.arguments["destination"] = pathlib.Path(self.arguments["destination"])
        self.arguments["sources"] = set(
            map(
                lambda source: pathlib.Path(source),
                self.arguments["sources"],
            ),
        )
        self.arguments["month"] = str(self.arguments["month"]).rjust(2, "0")
        self.arguments["year"] = str(self.arguments["year"]).rjust(4, "0")

    def __determine_initials(self):
        """Get initials from the title."""
        self.arguments["initials"] = "".join(
            filter(
                lambda character: character.isupper(),
                self.arguments["title"],
            ),
        )


def count_files(sources, desired_filetypes):
    """Count the number of files in a collection of sources."""
    file_count = 0
    for source in sources:
        for item in source.iterdir():
            filetype = item.suffix.lower()
            if filetype in desired_filetypes:
                file_count += 1

    return file_count


# Main entry point of the script.
parser = Parser()
parser.parse_arguments()

# Determine the number of places required for the image and video indexes.
image_count = count_files(parser.arguments["sources"], KNOWN_IMAGE_TYPES)
video_count = count_files(parser.arguments["sources"], KNOWN_VIDEO_TYPES)
image_index_places = len(str(image_count))
video_index_places = len(str(video_count))

# Create the Path objects for the main destination and the video destination.
destination = parser.arguments["destination"] / TITLE_FORMAT.format(
    year=parser.arguments["year"],
    month=parser.arguments["month"],
    title=parser.arguments["title"],
)
video_destination = destination / DEFAULT_CLIPS_DIRECTORY

# If either destination doesn't exist, create it.
if image_count > 0 and not destination.exists():
    destination.mkdir(parents=True)
if video_count > 0 and not video_destination.exists():
    video_destination.mkdir(parents=True)

# Copy each image and video into the correct destination.
image_index = 1
video_index = 1
for source in parser.arguments["sources"]:
    for item in source.iterdir():
        filetype = item.suffix.lower()
        if filetype in KNOWN_IMAGE_TYPES:
            shutil.copy2(
                item,
                destination / ITEM_FORMAT.format(
                    initials=parser.arguments["initials"],
                    sequence=str(image_index).rjust(image_index_places, "0"),
                    extension=filetype,
                ),
            )
            image_index += 1
        elif filetype in KNOWN_VIDEO_TYPES:
            shutil.copy2(
                item,
                video_destination / ITEM_FORMAT.format(
                    initials=parser.arguments["initials"],
                    sequence=str(video_index).rjust(video_index_places, "0"),
                    extension=filetype,
                ),
            )
            video_index += 1
        else:
            print("here")
            print("unknown file type")
            # handle weird file types
