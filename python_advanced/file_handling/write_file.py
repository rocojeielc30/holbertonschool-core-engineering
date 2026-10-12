#!/usr/bin/env python3
"""Defines a function that creates a file or overwrites a current and returns number of characters written."""


def write_file(filename="", text=""):
    """Return number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        new_file = file.write(text)
    return new_file
