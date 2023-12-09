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