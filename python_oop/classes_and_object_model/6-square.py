#!/usr/bin/env python3
"""Defines a Square class with a size, a position and a string form."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise the square with a size and a position."""
        self.size = size  # goes through the setter
        self.position = position  # goes through the setter

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

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating it."""
        if not self.__is_valid_position(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @staticmethod
    def __is_valid_position(value):
        """Return True if value is a tuple of 2 integers >= 0."""
        if type(value) is not tuple or len(value) != 2:
            return False
        for number in value:
            if type(number) is not int or number < 0:
                return False
        return True

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square drawn with # and offset by its position."""
        if self.__size == 0:
            return ""

        horizontal_offset, vertical_offset = self.__position
        blank_lines = [""] * vertical_offset
        row = " " * horizontal_offset + "#" * self.__size
        square_rows = [row] * self.__size
        return "\n".join(blank_lines + square_rows)

    def my_print(self):
        """Print the square, same as printing the object."""
        print(self)  # calls __str__
