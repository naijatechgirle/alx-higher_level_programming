#!/usr/bin/python3
'''
Writing an Object to a text file, using a JSON
'''

import json


def save_to_json_file(my_obj, filename):
    ''' writes an Object to a text file, using a JSON representation '''
    with open(filename, 'w') as open_file:
        open_file.write(json.dumps(my_obj))
