#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string"""


import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
      represented by a JSON string

    Args:
    - my_str: the JSON string to be represented

    Return:
    - the Python data structure
    """

    return json.loads(my_str)
