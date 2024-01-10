#!/usr/bin/python3
"""Module that adds all arguments to a Python list,
and then save them to a file
"""


import json
import sys
from os import path


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    file_name = "add_item.json"
    data = []

    if path.exists(file_name):
        data = load_from_json_file(file_name)

    data.extend(sys.argv[1:])
    save_to_json_file(data, file_name)
