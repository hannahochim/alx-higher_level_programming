#!/usr/bin/python3
"""Function defines a text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as n:
        for line in n:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
