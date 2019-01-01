"""
"""
import argparse

class Parser(argparse.ArgumentParser):
    """Class that handles command line arguments."""

    def __init__(self, *args, **kwargs):
        """Initialize super and turn off help functions."""
        super().__init__(*args, add_help=False, **kwargs)


    def parse_arguments(self):
        """Parse known arguments and save them."""
        self.arguments, self.unknown = self.parse_known_args()


    def add_arguments(self):
        """Add flags to the parser."""
        self.add_argument('-c', '--copy', action='store_true', default=None)
        self.add_argument('-m', '--move', action='store_true', default=None)

        self.add_argument('--unfollow')
        self.add_argument('-m', '--move')
        self.add_argument('-f', '--follow', nargs='+')
        self.add_argument('--man', action='store_true', default=None)
        self.add_argument('-c', '--crumb', action='store_true', default=None)


    def error(self, message):
        #"""In case of an error, show the user the help menu."""
        #utilities.throw_help()
        pass
