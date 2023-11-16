#!/usr/bin/python3
"""
This module defines the base class.
"""


class Base:
    """
    The Base class.
    """
    def __init__(self, id=None):
        """Initialize the Base instance."""
        self.id = id if id is not None else id_counter()
