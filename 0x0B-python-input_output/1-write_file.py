#!/usr/bin/python3
"""This writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """this function writes into a file
        Args:
        filename: The name of the file
        file to write into
        text: The text to write
        text to write into the file
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
