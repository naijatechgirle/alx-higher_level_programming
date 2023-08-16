#!/usr/bin/python3

"""
Writing a module for MyInt.
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
