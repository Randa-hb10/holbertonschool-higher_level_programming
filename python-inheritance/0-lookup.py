#!/usr/bin/python3
"""
0-lookup.py

This module contains a function `lookup` that returns the list of
available attributes and methods of any Python object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object (class, instance, built-in type, etc.)

    Returns:
        list: A list of strings representing the names of attributes
              and methods accessible on the object.
    """

    return dir(obj)

