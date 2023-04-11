#!/usr/bin/python3
"""this is a subclass."""


class MyList(list):
    """subclass inherited from list class."""

    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
