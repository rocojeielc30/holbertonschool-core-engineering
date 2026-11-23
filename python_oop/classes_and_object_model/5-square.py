#!/usr/bin/env python3
"""Defines a Square class that can print itself."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialise the square with a given size."""
        self.size = size  # goes through the setter

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
            return

        row = "#" * self.__size
        for _ in range(self.__size):
            print(row)