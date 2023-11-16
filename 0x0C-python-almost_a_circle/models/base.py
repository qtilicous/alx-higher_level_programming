#!/usr/bin/python3
"""
This module defines the Base class.
"""

import json


class Base:
    """
    The Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base instance.

        Args:
            id (int): The id of the instance (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.
        """
        filename = cls.__name__ + ".json"
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())

        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string.

        Returns:
            list: The list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: A double pointer to a dictionary.

        Returns:
            Base: An instance with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_str = file.read()
                obj_list = cls.from_json_string(json_str)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []


if __name__ == "__main__":
    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
