#!/usr/bin/python3
"""
Module of a append_after class
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file after each line containing a string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line to insert after each line.
    """
    with open(filename, mode='r') as file:
        lines = file.readlines()

    with open(filename, mode='w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
