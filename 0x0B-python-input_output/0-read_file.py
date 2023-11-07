#!/usr/bin/python3
"""
This module reads a text file and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())


if __name__ == "__main__":
    read_file("my_file_0.txt")
