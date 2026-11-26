#!/usr/bin/env python3
"""A square shape built on top of Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A square: a rectangle whose sides are all the same length."""

    def __init__(self, size):
        """Check the size is valid, store it, then set up the rectangle."""
        # use the inherited checker before storing anything
        self.integer_validator("size", size)
        self.__size = size
        # a square is a rectangle with equal width and height
        super().__init__(size, size)

    def area(self):
        """Work out the area: size times size."""
        return self.__size * self.__size
