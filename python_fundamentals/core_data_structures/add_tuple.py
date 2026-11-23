#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)  # pad with zeros so there are always at least two values
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
