#!/usr/bin/python3
"""
Module of a Student class
"""


class Student:
    """Student class defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list of str): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        """
        Replace attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary with attribute names and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
