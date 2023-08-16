#!/usr/bin/python3
'''
Reading and printing the contents of a file
'''


def read_file(filename=""):
    ''' This reads file and prints contents '''
    with open(filename) as open_file:
        contents = open_file.read()
    print(contents, end="")
