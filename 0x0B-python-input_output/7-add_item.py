#!/usr/bin/python3
"""
This script adds command-line arguments to a list and saves it to a JSON file.
"""

import sys
import json


def add_arguments_to_list(args):
    try:
        with open('add_item.json', 'r') as file:
            my_list = json.load(file)
    except FileNotFoundError:
        my_list = []

        my_list.extend(args)

        with open('add_item.json', 'w') as file:
            json.dump(my_list, file)
