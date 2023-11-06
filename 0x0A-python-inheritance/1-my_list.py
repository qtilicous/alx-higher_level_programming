#!/usr/bin/python3
""" Module of a MyList class """


class MyList(list):
    """
    A custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        """
        print(sorted(self))
