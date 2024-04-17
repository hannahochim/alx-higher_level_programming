#!/usr/bin/python3
"""Defines a  file appending function"""


def append_write(filename="", text=""):
    """function appends a string to the end of file
        and returns the number of characters added
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
