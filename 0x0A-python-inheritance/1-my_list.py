#!/usr/bin/python3
"""class that print a list and sort it out"""


class MyList(list):
    """class that print a list and sort it out"""

    def print_sorted(self):
        """print_sorted - prints list in sorted manner in ascending order"""
        return print(sorted(self, reverse=False))
