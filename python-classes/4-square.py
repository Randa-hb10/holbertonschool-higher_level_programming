#!/usr/bin/python3
"""Defines a Square class with a private size attribute, getter, setter, and area method."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with optional size, using the setter for validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, validating type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
