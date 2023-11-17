#!/usr/bin/python3
"""
This module defines the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square (default is 0).
            y (int): The y-coordinate of the square (default is 0).
            id (int): The id of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.validate_non_negative_integer("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: A variable number of non-keyword arguments.
            **kwargs: A variable number of keyword arguments.
        """
        attributes = ["id", "size", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the square.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    def validate_non_negative_integer(self, name, value):
        """Validate that a value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
