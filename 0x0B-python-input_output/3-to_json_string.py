#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of a an object
    Args:
        my_obj - object string
    Returns:
        JSON representation
    """
    json_data = json.dumps(my_obj)
    return json_data
