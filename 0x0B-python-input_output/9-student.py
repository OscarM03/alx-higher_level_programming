#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """
    A class that defines a Student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(): Returns a dictionary representation of
        the student's attributes.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student's attributes.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
