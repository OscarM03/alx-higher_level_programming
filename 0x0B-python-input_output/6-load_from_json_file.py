#!/usr/bin/python3
"""
Defines a function that creates an Object from
a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from
    a “JSON file”
    Args:
        filename - name of the file
    """
    with open(filename, "r") as file:
        loaded_data = json.load(file)
    return loaded_data
