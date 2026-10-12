#!/usr/bin/env python3
"""Defines a function that creates a file or overwrites a current and returns number of characters written."""


def write_file(filename="", text=""):
    """Print the contents of the file"""
    with open(filename, "w", encoding="utf-8") as file:
        new_file = file.write(text)
    print(new_file)
    return new_file
