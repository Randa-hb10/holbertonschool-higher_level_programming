#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size attribute

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize the square with optional size, validating type and value."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
