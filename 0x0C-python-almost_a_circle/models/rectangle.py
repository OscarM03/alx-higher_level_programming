#!/usr/bin/python3
"""Modules imported"""
import json
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle, a subclass of the Base class.

    Attributes:
    - __width (int): Width of the rectangle.
    - __height (int): Height of the rectangle.
    - __x (int): X-coordinate of the top-left corner of the rectangle.
    - __y (int): Y-coordinate of the top-left corner of the rectangle.
    - id (int): Identifier of the rectangle (inherited from the Base class).

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None): Constructor
    to initialize a Rectangle instance.
    - width (property): Getter for the width attribute.
    - width (setter): Setter for the width attribute.
    - height (property): Getter for the height attribute.
    - height (setter): Setter for the height attribute.
    - x (property): Getter for the x attribute.
    - x (setter): Setter for the x attribute.
    - y (property): Getter for the y attribute.
    - y (setter): Setter for the y attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate of the top-left corner of the rectangle.
        - y (int): Y-coordinate of the top-left corner of the rectangle.
        - id (int): Identifier of the rectangle (inherited from the Base
        class).
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.__y = value
