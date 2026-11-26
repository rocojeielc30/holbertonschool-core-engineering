#!/usr/bin/env python3
"""Shapes that all share area and perimeter, used through duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """A general shape: a blueprint every real shape must follow."""

    @abstractmethod
    def area(self):
        """Every shape must work out its area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape must work out the distance around it."""
        pass


class Circle(Shape):
    """A circle, described by its radius."""

    def __init__(self, radius):
        """Remember the circle's radius."""
        self.radius = radius

    def area(self):
        """Work out the area: pi times radius squared."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Work out the distance around: 2 times pi times radius."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A rectangle, described by its width and height."""

    def __init__(self, width, height):
        """Remember the rectangle's width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Work out the area: width times height."""
        return self.width * self.height

    def perimeter(self):
        """Work out the distance around: twice width plus height."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print any shape's area and perimeter, whatever kind it is."""
    # no type checks: if it has area() and perimeter(), it works
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
