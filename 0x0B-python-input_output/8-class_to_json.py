#!/usr/bin/python3
""" Module for class to JSON function
"""


def class_to_json(obj):
    """ Convert an object into a JSON-serializable dictionary

    Args:
        obj: The object to be converted

    Returns:
        dict: A dictionary representing the object's attributes
    """
    return obj.__dict__
