#!/usr/bin/python3
"""class of a Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class of a square that inherit from a rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area of a square"""
        return self.size * self.size
