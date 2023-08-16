#!/usr/bin/python3
'''
writing files
'''


def write_file(filename="", text=""):
    ''' This writes text to file '''
    with open(filename, 'w') as open_file:
        open_file.write(text)
        count = open_file.tell()
    return count
