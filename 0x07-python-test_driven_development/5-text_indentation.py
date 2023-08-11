#!/usr/bin/python3
"""This defines a function that prints a text
with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
       This Prints indent text
    """
    if type(text) != str or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    ben = 0
    for a in text:
        if a == '?' or a == ':' or a == '.':
            print(a, end="\n\n")
            ben = 1
        else:
            if ben == 0:
                print(a, end="")
            else:
                if a == ' ' or a == '\t':
                    pass
                else:
                    print(a, end="")
                    ben = 0
