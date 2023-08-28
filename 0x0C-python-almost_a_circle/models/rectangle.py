#!/usr/bin/python3
"""
Implementing a Rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """Implementation of Rectangle
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initializating
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """representation of string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name:  str, value: object, greater_equal=False):
        """typing and value validation
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """the width getter
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """the width setter
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """the height getter
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """the height setter
        """
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """the x getter
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """the x setter
        """
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """the y getter
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """the y setter
        """
        self.check_type_value('y', y, True)
        self.__y = y

    def area(self) -> int:
        """the area
        """
        return self.width * self.height

    def display(self):
        """this prints * shape of the rectangle
        """
        print('\n'*self.y, end='')
        for l in range(self.height):
            print(' '*self.x + '#'*self.width)

    def update(self, *args, **kwargs):
        """the update rectangle attributes
        """

        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> int:
        """the rectangle to dictionary
        """

        return {
            'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width}

