#!/usr/bin/python3

"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class serving as a base for geometry-related classes.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
