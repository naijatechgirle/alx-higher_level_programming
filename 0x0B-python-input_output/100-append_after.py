#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""


    with open(filename, 'r+', encoding='utf-8') as current_file:
        lines = current_file.readlines()
        current_file.seek(0)
        for c, line in enumerate(lines):

            if search_string in line:
                lines[c] = line + new_string
                current_file.writelines(lines)
