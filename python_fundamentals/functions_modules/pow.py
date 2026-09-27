#!/usr/bin/env python3
def pow(a, b):
    i = 1
    sum = a
    if b == 0:
        sum = 1
    elif b < 0:
        i = -1
        a = a * -1
        while i != b:
            sum = sum * a
            i -= 1
    else:
        while i != b:
            sum = sum * a
            i += 1
    return (sum)
