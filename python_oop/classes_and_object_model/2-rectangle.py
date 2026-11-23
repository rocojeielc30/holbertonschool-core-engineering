#!/usr/bin/env python3
"""Defines a Rectangle class with area and perimeter methods."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise the rectangle with a width and a height."""
        self.width = width  # goes through the setter
        self.height = height  # goes through the setter

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating it."""
        self.__validate_dimension("width", value)
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating it."""
        self.__validate_dimension("height", value)
        self.__height = value

    @staticmethod
    def __validate_dimension(name, value):
        """Raise an error if value is not an integer >= 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if a side is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
