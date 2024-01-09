#!/usr/bin/python3
""" function that check if a obj is an instance of an class """


def is_same_class(obj, a_class):
    """check if a function is an instance of a class"""

    if isinstance(obj, a_class):
        return True
    else:
        False
