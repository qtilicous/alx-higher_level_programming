#!/usr/bin/python3
"""
This module creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and creates an object from it.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
