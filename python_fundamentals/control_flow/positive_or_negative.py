#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
less = f"{number} is negative"
is_zero = f"{number} is zero"
positive = f"{number} is positive"

if number < 0:
    print(less)
elif number == 0:
    print(is_zero)
else:
    print(positive)
