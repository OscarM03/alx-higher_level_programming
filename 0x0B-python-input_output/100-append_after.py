#!/usr/bin/python3
"""
A functions that appends a string in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new line after each line containing a specific string in a file.

    Args:
        filename (str): The path of the file to be modified.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after each line
        containing the search string.

    Returns:
        None
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_lines.append(line)
        if search_string in line:
            modified_lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(modified_lines)
