#!/usr/bin/env python3
"""A starting point that other shape classes can build on."""


class BaseGeometry:
    """A general shape with tools that all shapes can share."""

    def area(self):
        """Every shape works out area differently, so this one just says it can't."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is a whole number bigger than 0, and complain if it isn't."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))  # not a whole number
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))  # zero or negative