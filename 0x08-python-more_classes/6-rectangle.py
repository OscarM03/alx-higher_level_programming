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
    - area(self): Calculates and returns the area of the rectangle.
    - perimeter(self): Calculates and returns the perimeter of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: Area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        - int: Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        If width or height is equal to 0, returns an empty string.
        Otherwise, returns a string with rows and columns of # characters.

        Returns:
        - str: String representation of the rectangle.
        """
        rectangle_string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                rectangle_string += "#" * self.__width
                if i < self.__height - 1:
                    rectangle_string += "\n"
            return rectangle_string

    def __repr__(self):
        """
        Return a string representation of the Rectangle object.

        The returned string is a valid Python expression that,
        when passed to
        eval(), would recreate a new Rectangle object with the
        same width and
        height.

        Returns:
            str: A string representation of the Rectangle object.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Destructor for the Rectangle class.

        This method is automatically called when an instance of the Rectangle
        class is about to be destroyed (deleted). It prints the message
        "Bye rectangle..." to indicate that the object is being deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
