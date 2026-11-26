#!/usr/bin/env python3
"""A dragon that picks up swimming and flying from small add-on classes."""


class SwimMixin:
    """An add-on that gives a creature the ability to swim."""

    def swim(self):
        """Say the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """An add-on that gives a creature the ability to fly."""

    def fly(self):
        """Say the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon: swims and flies thanks to the add-ons, and roars itself."""

    def roar(self):
        """Say the dragon roars."""
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()

    dragon.swim()
    dragon.fly()
    dragon.roar()
