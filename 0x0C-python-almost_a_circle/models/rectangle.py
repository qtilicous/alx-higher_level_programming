#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class, a subclass of Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle (default is 0).
            y (int): The y-coordinate of the rectangle (default is 0).
            id (int): The id of the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.validate_non_negative_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.validate_non_negative_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_non_negative_integer(self, attribute, value):
        """
        Validate that the value is a non-negative integer.

        Args:
            attribute (str): The name of the attribute being validated.
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))


if __name__ == "__main__":
    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
