#!/usr/bin/python3

"""
Writing a module for Rectangle and BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""

    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
