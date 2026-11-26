#!/usr/bin/env python3
"""A flying fish that gets abilities from both a fish and a bird."""


class Fish:
    """A fish, which swims and lives in water."""

    def swim(self):
        """Say the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Say where the fish lives."""
        print("The fish lives in water")


class Bird:
    """A bird, which flies and lives in the sky."""

    def fly(self):
        """Say the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Say where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish: part fish, part bird, with its own versions."""

    def fly(self):
        """Say the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Say the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Say the flying fish lives in both places."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()

    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    # the order Python searches the classes for a method
    print(FlyingFish.mro())
