#!/usr/bin/python3
"""Module that adds all arguments to a Python list,
and then save them to a file
"""


import sys
import json
import os.path


filename = "add_item.json"
my_list = []

if os.path.isfile(filename):
    my_list = json.load(open(filename))

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

json.dump(my_list, open(filename, mode='w'))
