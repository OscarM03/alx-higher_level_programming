#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """opens a text file and write a string to it"""
    with open(filename, "w") as file:
      chars_written = file.write(text)
    return chars_written
