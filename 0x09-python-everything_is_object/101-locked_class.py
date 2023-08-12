#!/usr/bin/python3
"""class contains predefined number of slots"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes,
       except if the new instance attribute is called first_name"""
    __slots__ = ['first_name']
