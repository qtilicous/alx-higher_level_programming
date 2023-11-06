#!/usr/bin/python3

class MyList(list):
    """
    A custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        """
        print(sorted(self))
