#!/usr/bin/env python3
"""Defines a function that reads and prints the contents of a file."""

def read_file(filename=""):
    """Print the contents of the file"""
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    print(text, end="")
