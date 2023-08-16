#!/usr/bin/python3

"""
Writing a module for BaseGeometry.
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
