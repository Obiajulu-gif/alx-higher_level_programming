#!/usr/bin/python3
"""
Module that defines the MyList class.
"""

class MyList(list):
    """
    A custom list class that provides additional functionality.

    Methods:
        print_sorted: Prints the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)