#!/usr/bin/python3
"""Defines a Student class"""
import sys
import os


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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student's attributes.

        Args:
            attrs (list): A list of strings representing attribute
            names to retrieve.
                          If None, retrieves all attributes.

        Returns:
            dict: A dictionary containing the specified or all attributes.
        """
        if isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if
                    hasattr(self, key)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        values from the provided dictionary.

        Args:
        json (dict): A dictionary where each key is a public
        attribute name,
                     and the corresponding value is the new
                     value for that attribute.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
