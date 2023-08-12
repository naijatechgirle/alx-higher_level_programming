#!/usr/bin/python3

"""
This defines a class rectangle
"""


class Rectangle:
    """The Rectangle class"""

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This is Initializing the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Get string the representation"""
        width = self.__width
        height = self.__height
        symbol = self.print_symbol
        string = ""
        if width == 0 or height == 0:
            return string
        for a in range(height):
            for b in range(width):
                string = string + str(symbol)
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        """Get the string."""
        width = self.__width
        height = self.__height
        string = "Rectangle(" + str(width) + \
            ", " + str(height) + ")"
        return string

    def __del__(self):
        """deleted"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This returns the biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a1 = rect_1.area()
        a2 = rect_2.area()
        if a1 == a2:
            return rect_1
        elif a1 > a2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """This returns a new Rectangle"""
        return cls(size, size)
