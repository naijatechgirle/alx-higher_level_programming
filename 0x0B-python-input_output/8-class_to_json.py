#!/usr/bin/python3
'''
Returing the dictionary description with simple data structure
'''


def class_to_json(obj):
    ''' Returns dictionary description with data list for
    JSON serialization of an object '''
    return obj.__dict__
