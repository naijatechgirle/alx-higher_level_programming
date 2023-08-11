#!/usr/bin/python3
"""This defines a name printing function"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person full name.
    """
    if type(first_name) != str:
        raise TypeError('First_name must be a string')
    if type(last_name) != str:
        raise TypeError('Last_name must be a string')
    print("My name is " + first_name + " " + last_name)
