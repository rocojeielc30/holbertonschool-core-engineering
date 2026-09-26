#!/usr/bin/env python3
def islower(c):
    """Check if a character is lowercase."""
    value = ord(c)
    if 97 <= value <= 122:
        return True
    else:
        return False
