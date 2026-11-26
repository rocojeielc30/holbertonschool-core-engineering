#!/usr/bin/env python3
"""A starting point that other shape classes can build on."""


class BaseGeometry:
    """A general shape with tools that all shapes can share."""

    def area(self):
        """Shapes work out area differently, so this one can't."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check value is a whole number above 0, or complain."""
        # not a whole number
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        # zero or negative
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
