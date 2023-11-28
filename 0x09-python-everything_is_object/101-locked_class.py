#!/usr/bin/python3
class LockedClass:
    """
    LockedClass: A class with restricted attribute creation.

    Attributes:
    - first_name: Allowed attribute for storing the first name.
    """

    __slots__ = ['first_name']

    def __init__(self, value=""):
        """
        Initializes a LockedClass instance.

        Args:
        - value (str): The initial value for the 'first_name' attribute.
        """
        self.first_name = value
