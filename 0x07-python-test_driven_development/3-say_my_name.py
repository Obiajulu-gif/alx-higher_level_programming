#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    fuction that print out the full name

    Args:
    - first_name: get the first name of a user
    - last_name: get the last_name of a user

    Return:
    - return the fullname of the user
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        full_name = first_name + " " + last_name
    else:
        full_name = first_name
    print("My name is", full_name)
