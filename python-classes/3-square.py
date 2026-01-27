#!/usr/bin/python3
"""Defines a Square class with a private size attribute and area method."""


class Square:
     """Defines a Square class with size validation and area calculation."""

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
