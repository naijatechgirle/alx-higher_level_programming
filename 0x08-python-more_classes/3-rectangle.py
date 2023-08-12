#!/usr/bin/python3

"""
This defines a class Rectangle
"""


class Rectangle:
    """The Rectangle class"""

    def __init__(self, width=0, height=0):
        """This is Initializing the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """Set the width"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """Set the height"""
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue

    def area(self):
        """Calculate the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        """Get the string representation"""
        width = self.__width
        height = self.__height
        string = ""
        if width == 0 or height == 0:
            return string
        for a in range(height):
            for b in range(width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]
