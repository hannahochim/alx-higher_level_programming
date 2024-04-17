#!/usr/bin/python3
"""Defines a string to Json functio"""
import json


def to_json_string(my_obj):
    """function returns a Json representation
        of a string
    """
    return json.dumps(my_obj)
