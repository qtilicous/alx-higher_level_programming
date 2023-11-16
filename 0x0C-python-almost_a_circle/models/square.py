#!/usr/bin/python3
"""
This module defines the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class, a subclass of Rectangle.
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


if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    s2 = Square(2, 2)
    print(s2)
    print(s2.size)
    s2.size = 3
    print(s2)

    try:
        s2.size = -3
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.size)
    s3.update(4)
    print(s3)
    s3.update(5, 1)
    print(s3)
    s3.update(6, 1, 2)
    print(s3)
    s3.update(7, 1, 2, 3)
    print(s3)
    s3.update(y=1, size=7)
    print(s3)
    s3.update(size=7, id=89, y=1)
    print(s3)
