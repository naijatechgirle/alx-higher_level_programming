#!/usr/bin/python3
"""
Writing a module for MyList
"""


class MyList(list):
    """This is MyList class."""

    def print_sorted(self):
        """Print the list in ascending sort."""
        print(sorted(self))
