#!/usr/bin/python3

"""
Writing a module for Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square"""

    def __init__(self, size):
        """Initializing"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area"""
        return self.__size ** 2
