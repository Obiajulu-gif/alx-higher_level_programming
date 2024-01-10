#!/usr/bin/python3
"""
module that return the dictionary description
with simple data structure for JSON Serialization of an object
"""


def class_to_json(obj):
    """function that return dictionary description
    with a simple data structure for JSON
    Serialization of an Object

    Args:
    - obj: Object from other class

    Return:
    - return dictionary description for JSON serilaization
    """
    class_dict = obj.__dict__.copy()

    for key, value in class_dict.items():
        if isinstance(value, (bool, int, str, list, dict)):
            class_dict[key] = value
    return class_dict
