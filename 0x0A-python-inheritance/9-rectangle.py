#!/usr/bin/python3

"""
Writing a module for Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""

    def __init__(self, width, height):
        """Initalizing"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the  string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
