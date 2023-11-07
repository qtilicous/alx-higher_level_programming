#!/usr/bin/python3
"""
This module appends a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8).

    Args:
        filename (str): The name of the text file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
