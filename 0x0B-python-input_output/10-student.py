#!/usr/bin/python3
"""class that define a student"""


class Student:
    """
    class of a Student

    Public instance attributes:
        self.first_name
        self.last_name
        self.age

    Public Method:
    def to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of Student instance"""
        class_dict = self.__dict__.copy()

        for key, value in class_dict.items():
            if isinstance(value, (bool, int, str, list, dict)):
                class_dict[key] = value
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr 
                                           in attrs):
            class_dict = {key: value for key, value in class_dict.items() if key in attrs}
                    
        return class_dict
