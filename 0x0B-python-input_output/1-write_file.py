#!/usr/bin/python3
"""
This module writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).

    Args:
        filename (str): The name of the text file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
