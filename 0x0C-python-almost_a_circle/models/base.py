#!/usr/bin/python3
"""Modules imported"""
import json


class Base:
    """Base class for managing id attribute in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Parameters:
        - id (int or None): If provided, assigns the id attribute
        with the given value.
                    If None, increments __nb_objects and
                    assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file
        """
        new_list_obj = []
        if list_objs is not None:
            for obj in list_objs:
                new_list_obj.append(obj.to_dictionary())

            j_data = cls.to_json_string(new_list_obj)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(j_data)

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of
        the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
