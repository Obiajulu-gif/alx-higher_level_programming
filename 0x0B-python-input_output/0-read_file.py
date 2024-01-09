#!/usr/bin/python3
"""Function to read text file"""


def read_file(filename=""):
    """function that will read a .txt file

    Args:
    - filename: the name of the file

    Return:
    - Return all the text to the stdout
    """

    with open(filename, "r", encoding="utf-8") as filedoc:
        fp = filedoc.read()
        print(fp, end='')
