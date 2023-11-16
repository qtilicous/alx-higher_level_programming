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
        """Initialize the Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
