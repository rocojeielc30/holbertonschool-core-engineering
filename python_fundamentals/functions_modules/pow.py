#!/usr/bin/env python3
def pow(a, b):
    i = 1
    if b == 0:
        sum = 1
    else:
        sum = a
        while i < b:
            sum = sum * a
            i += 1
    print(sum)
    return (sum)
