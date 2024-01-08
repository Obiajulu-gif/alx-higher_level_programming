#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    :param obj: The object to lookup.
    :return: A list of attributes and methods.
    """
    return dir(obj)
