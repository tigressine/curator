"""
"""
import argparse
import utilities


class Parser(argparse.ArgumentParser):
    """Class that handles command line arguments."""

    def __init__(self, *args, **kwargs):
        """Initialize super and add some arguments."""
        super().__init__(*args, add_help=False, **kwargs)

        self.add_argument("destination")
        self.add_argument("sources", nargs="+")
        self.add_argument("--date")
        self.add_argument("--method")
        """
        self.add_argument(
            "--ignore-unknown-filetypes",
            action="store_true",
            default=None
        )
        """
        # add safety

    def parse_arguments(self):
        """Parse known arguments and save them."""
        self.arguments, self.unknown = self.parse_known_args()
        self.arguments = vars(self.arguments)

    '''
    def error(self, message):
        """If any parsing error occurs, help the user."""
        utilities.throw_help()
    '''
