#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt:
    """inherit the int class from the in-built int class"""
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        if self.__value == other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__value != other:
            return True
        else:
            return False

    def __str__(self):
        return "{}".format(self.__value)
