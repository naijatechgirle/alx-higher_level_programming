#!/usr/bin/python3
'''
A class student that defines a student.
'''


class Student:
    ''' The Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Initializing the student class '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Returning Dictionary to JSON '''
        return self.__dict__
