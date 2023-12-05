#!/usr/bin/python3
"""No module imported"""


def read_file(filename=""):
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
