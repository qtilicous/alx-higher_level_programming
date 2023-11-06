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

    def integer_validator(self, name, value):
        """
        Validates the given value.
        Args:
            name (str): A string name for the value.
            value: The value to validate.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
