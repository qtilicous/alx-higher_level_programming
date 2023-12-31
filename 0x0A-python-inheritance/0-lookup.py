#!/usr/bin/python3
""" Module of a lookup class """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes and methods.
    """
    return dir(obj)
