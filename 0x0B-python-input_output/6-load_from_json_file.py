#!/usr/bin/python3
"""Function to create object from json file"""
import json


def load_from_json_file(filename):
    """function creates an object from a Json file"""
    with open(filename, 'r') as f:
        return json.load(f)
