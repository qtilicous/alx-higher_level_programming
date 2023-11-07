#!/usr/bin/python3
"""
This script adds command-line arguments to a list and saves it to a JSON file.
"""
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_to_list_and_save(args, filename):
    """
    Adds command-line arguments to a Python list and saves it to a JSON file.

    Args:
        args (list): The list of command-line arguments.
        filename (str): The name of the JSON file to save the list to.

    Returns:
        None
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)
