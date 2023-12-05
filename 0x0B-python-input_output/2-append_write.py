#!/usr/bin/python3
"""Defines a function that appends text to a file"""


def append_write(filename="", text=""):
    """
    A function that opens a file and appends a text to the file
    Args:
        filename - name of the file
        text - text to be appended
    Returns:
        The number of chars appended
    """
    with open(filename, "a") as file:
        chars = file.write(text)
    return chars
