#!/usr/bin/env python3
"""A rectangle shape built on top of BaseGeometry."""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        """Check both sides are valid, then store them privately."""
        # use the parent's checker on each side first
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
