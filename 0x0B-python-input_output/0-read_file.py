#!/usr/bin/python3
"""Defines a function that reads text from a file"""


def read_file(filename=""):
    """
    Function that reads a text file
    Args:
        filename - name of the file to be read
    """
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
