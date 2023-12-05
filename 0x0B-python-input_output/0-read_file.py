#!/usr/bin/python3
"""A simple script to read and print the contents of a UTF-8 encoded text file."""


def read_file(filename=""):
    """
    Read the contents of a UTF-8 encoded text file and print it to stdout.

    Parameters:
    - filename (str): The path to the file to be read. If not provided, the function does nothing.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - UnicodeDecodeError: If there is an issue decoding the file as UTF-8.

    Example:
    >>> read_file("example.txt")
    This is the content of the example file.

    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            print(file.read(), end="")
    except FileNotFoundError:
        print(f"Error: File not found - {filename}")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file as UTF-8 - {filename}")

# Example usage:
file_path = 'path/to/your/file.txt'
read_file(file_path)
