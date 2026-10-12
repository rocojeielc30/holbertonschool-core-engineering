#!/usr/bin/env python3
"""Defines a function that appends and returns the number of characters"""


def append_write(filename="", text=""):
    """Returns the number of characters that has been appended to the file"""
    with open(filename, "a", encoding="utf-8") as file:
        new_file = file.write(text)
    return new_file
