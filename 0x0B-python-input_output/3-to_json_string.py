#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    Args:
    - my_obj: the object to be represented

    Return:
    - the JSON representation
    """

    return json.dumps(my_obj)
