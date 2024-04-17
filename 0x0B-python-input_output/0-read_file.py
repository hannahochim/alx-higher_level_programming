#!/usr/bin/python3
"""This defines a funtion to read file"""


def read_file(filename=""):
    """Print file content to stdout"""
    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read(), end="")
