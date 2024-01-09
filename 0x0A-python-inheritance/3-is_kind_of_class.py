#!/usr/bin/python3
"""function that check for inherit object instance"""


def is_kind_of_class(obj, a_class):
    """
    check if an obj is a inherit instance

    Args:
    - obj: object to be check
    - instance to be checked

    Return:
    - return True if it's a inhert object
    """

    return isinstance(obj, a_class)
