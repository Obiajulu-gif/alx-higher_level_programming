#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation

    Args:
    - my_obj: the object to be written
    - filename: the file to be written

    Return:
    - nothing
    """

    with open(filename, mode="w", encoding="utf-8") as fileDoc:
        json.dump(my_obj, fileDoc)
    return
