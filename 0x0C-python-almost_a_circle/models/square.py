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
        """Initialize the Square instance."""
        super().__init__(size, size, x, y, id)
