#!/usr/bin/python3
"""function that write a string to a text file"""


def write_file(filename="", text=""):
    """
    Function that write a string to a text file

    Args:
    -filename: this will carry the name of the file
    -text: this will carry rhe string we want to write

    Return:
    return the number of character that is written
    """

    with open(filename, "w", encoding="utf-8") as fileDoc:

        return fileDoc.write(text)
