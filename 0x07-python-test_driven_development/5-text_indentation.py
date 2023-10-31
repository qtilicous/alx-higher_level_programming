#!/usr/bin/python3
"""
Module of a text_indentation class.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?' and ':'

    Args:
        text (str): The text to be indented.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    print(text[start:].strip())
