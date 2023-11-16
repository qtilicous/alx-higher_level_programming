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

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using '#' characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: A variable number of non-keyword arguments.
            **kwargs: A variable number of keyword arguments.
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == "__main__":
    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

    r4 = Rectangle(4, 6)
    r4.display()

    print("---")

    r5 = Rectangle(2, 2)
    r5.display()

    r6 = Rectangle(4, 6, 2, 1, 12)
    print(r6)

    r7 = Rectangle(5, 5, 1)
    print(r7)

    r8 = Rectangle(2, 3, 2, 2)
    r8.display()

    print("---")

    r9 = Rectangle(3, 2, 1, 0)
    r9.display()

    r10 = Rectangle(10, 10, 10, 10)
    print(r10)

    r10.update(height=1)
    print(r10)

    r10.update(width=1, x=2)
    print(r10)

    r10.update(y=1, width=2, x=3, id=89)
    print(r10)

    r10.update(x=1, height=2, y=3, width=4)
    print(r10)
