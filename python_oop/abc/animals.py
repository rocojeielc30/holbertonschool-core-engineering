#!/usr/bin/env python3
"""Animals that must each say what sound they make."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """A general animal: a blueprint, not something you create directly."""

    @abstractmethod
    def sound(self):
        """Every animal must say what sound it makes."""
        pass


class Dog(Animal):
    """A dog, which is a kind of animal."""

    def sound(self):
        """A dog barks."""
        return "Bark"


class Cat(Animal):
    """A cat, which is a kind of animal."""

    def sound(self):
        """A cat meows."""
        return "Meow"
