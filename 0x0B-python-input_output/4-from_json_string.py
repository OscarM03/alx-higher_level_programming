#!/usr/bin/python3
"""
Defines a function that returns an object
(Python data structure)represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object
    (Python data structure)represented by a JSON string
    Args:
        my_str - string to be deserialized
    Returns:
        (Python data structure)represented by a JSON string
    """
    python_str = json.loads(my_str)
    return python_str
