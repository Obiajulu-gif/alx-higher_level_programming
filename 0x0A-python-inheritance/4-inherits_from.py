#!/usr/bin/python3
"""check if an object is an instance of a class that inherited
 (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """
    Checking for an inherited object instance

    Args:
    - obj: object to be checked
    - a_class: class to be checked

    Return:
    - Return True if found or False if not found
    """

    return isinstance(obj, a_class) and issubclass(type(obj), a_class)
