#!/usr/bin/python3
""" lookup module determines the attributes and methods of an object."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    :param obj: The object to lookup.
    :return: A list of attributes and methods.
    """
    return dir(obj)
