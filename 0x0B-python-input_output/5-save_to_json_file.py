#!/usr/bin/python3
"""Defines a function that writes an Object to a
    text file, using a JSON representation
    """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj - data
        filename - name of the file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
