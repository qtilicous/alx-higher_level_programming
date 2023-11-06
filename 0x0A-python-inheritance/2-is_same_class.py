#!/usr/bin/python3
""" Module of a is_same_class """


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the class; else False

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class; else False.
    """
    return type(obj) is a_class
