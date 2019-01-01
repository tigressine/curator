"""
"""
import argparse
import utilities

class Parser(argparse.ArgumentParser):
    """Class that handles command line arguments."""

    def __init__(self, *args, **kwargs):
        """Initialize super and add some arguments."""
        super().__init__(*args, add_help=False, **kwargs)

        self.add_arguments()


    def add_arguments(self):
        """Add all supported arguments to the parser."""
        self.add_argument('destination')
        self.add_argument('inputs', nargs='+')
        self.add_argument('--date')

        # The copy and move flags are mutually exclusive.
        transfer_method_group = self.add_mutually_exclusive_group()
        transfer_method_group.add_argument(
            '--copy',
            action='store_true',
            default=None
        )
        transfer_method_group.add_argument(
            '--move',
            action='store_true',
            default=None
        )

        # All unknown filetype handling flags are mutually exclusive.
        unknown_filetypes_handler_group = self.add_mutually_exclusive_group()
        unknown_filetypes_handler_group.add_argument(
            '--copy-unknown-filetypes',
            action='store_true',
            default=None
        )
        unknown_filetypes_handler_group.add_argument(
            '--move-unknown-filetypes',
            action='store_true',
            default=None
        )
        unknown_filetypes_handler_group.add_argument(
            '--ignore-unknown-filetypes',
            action='store_true',
            default=None
        )


    def parse_arguments(self):
        """Parse known arguments and save them."""
        self.arguments, self.unknown = self.parse_known_args()


    def error(self, message):
        """If any parsing error occurs, help the user."""
        utilities.throw_help()
