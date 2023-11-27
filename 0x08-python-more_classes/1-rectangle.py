#!/usr/bin/python3
"""Creates a rectangle class"""


class Rectangle:
    """
    Defines a rectangle.

    Attributes:
    - width (int): Width of the rectangle.
    - height (int): Height of the rectangle.

    Methods:
    - __init__(self, width=0, height=0): Initializes a rectangle.
    - width (property): Getter method for the width attribute.
    - width (setter): Setter method for the width attribute.
    - height (property): Getter method for the height attribute.
    - height (setter): Setter method for the height attribute.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        - int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        - value (int): Width value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        - int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        - value (int): Height value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
