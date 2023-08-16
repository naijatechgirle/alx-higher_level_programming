#!/usr/bin/python3
'''
Creating an object from a JSON files
'''

import json


def load_from_json_file(filename):
    ''' Creates an object from JSON file '''
    with open(filename, 'r') as open_file:
        return json.load(open_file)
