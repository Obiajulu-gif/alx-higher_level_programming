#!/usr/bin/python3
"""class of a BaseGeometry"""


class BaseGeometry:
    """class of a BaseGeometry"""

    def area(self):
        """calculate for area
        Raises:
            Exception: if area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value
        Args:
            name (str): name of the value
            value (int): value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
