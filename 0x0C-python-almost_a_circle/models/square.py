#!/usr/bin/python3
"""class of a square that inherit a Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherit from a Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attribute based on the provided arguments
        and keyword argument"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        attributes = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attributes}
