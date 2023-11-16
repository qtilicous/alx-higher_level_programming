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
            self.id, self.x, self.y, self.width
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


if __name__ == "__main__":
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
