"""
"""
import shutil
import pathlib
import argparse
import constants


class Parser(argparse.ArgumentParser):
    """Class that handles command line arguments."""

    def __init__(self, *args, **kwargs):
        """Initialize super and add some arguments."""
        super().__init__(*args, add_help=False, **kwargs)

        self.add_argument("destination", type=pathlib.Path)
        self.add_argument("sources", nargs="+", type=pathlib.Path)
        self.add_argument("--date", default=None)
        self.add_argument("--title", default=constants.DEFAULT_TITLE)
        self.add_argument(
            "--transfer-method",
            default=constants.DEFAULT_TRANSFER_METHOD,
            choices=constants.TRANSFER_METHOD_CHOICES,
        )
        self.add_argument(
            "--unknown-extensions",
            default=constants.DEFAULT_UNKNOWN_EXTENSION_HANDLER,
            choices=constants.UNKNOWN_EXTENSION_HANDLER_CHOICES,
        )
        self.add_argument(
            "--title-format",
            default=constants.DEFAULT_TITLE_FORMAT,
        )
        self.add_argument(
            "--item-format",
            default=constants.DEFAULT_ITEM_FORMAT,
        )
        # add safety

    def parse_arguments(self):
        """Parse known arguments and save them."""
        self.arguments, self.unknown = self.parse_known_args()
        self.arguments = vars(self.arguments)

    '''
    def error(self, message):
        """If any parsing error occurs, help the user."""
        throw_help()


def throw_help():
    print("yikes")
    exit(0)
'''
def copy_file(item, destination, target_format, target_format_arguments):
    """"""
    target = pathlib.Path(destination) / target_format.format(**target_format_arguments)
    shutil.copy2(str(item), str(target))
