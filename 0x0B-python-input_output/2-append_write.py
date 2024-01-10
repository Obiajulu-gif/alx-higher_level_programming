#!/usr/bin/python3
"""function that append a string at the end"""


def append_write(filename="", text=""):
    """
    Function that append a string at the end of text file

    Args:
    - filename: the name of the file
    - text: the  text tobe append

    Return:
    - it return the number of charater written
    """

    with open(filename, mode="a", encoding="utf-8") as fileDoc:
        return fileDoc.write(text)
