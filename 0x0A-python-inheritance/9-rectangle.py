#!/usr/bin/python3
"""class of a Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return a well formatted string of an object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
