#!/usr/bin/python3
"""class that print a list and sort it out"""


class MyList(list):
    """class that print a list and sort it out"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        return print(sorted(self))
