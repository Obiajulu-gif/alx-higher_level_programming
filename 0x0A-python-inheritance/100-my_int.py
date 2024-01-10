#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits from int with inverted == and != operators"""

    def __eq__(self, other):
        """Override == operator to return the inverted result"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to return the inverted result"""
        return super().__eq__(other)
