#!/usr/bin/python3
'''
Returning an object represented by JSON
'''

import json


def from_json_string(my_str):
    ''' Returns an object from JSON string '''
    return json.loads(my_str)
