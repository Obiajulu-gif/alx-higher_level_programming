#!/usr/bin/python3
""" List module creates class inheriting from list object."""


class MyList(list):
    """ Class MyList inherits from list"""

    def print_sorted(self):
        """print_sorted - prints list in sorted manner in ascending order"""

        print(sorted(self))
