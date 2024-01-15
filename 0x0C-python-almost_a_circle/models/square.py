#!/usr/bin/python3
"""class of a square that inherit a Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherit from a Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)
