#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

if number < 0:
    number = number * -1
    last_digit = number % 10
    number = number * -1
else:
    last_digit = number % 10

less = f"Last digit of {number} is {last_digit} and is less than 6 and not 0"
is_zero = f"Last digit of {number} is {last_digit} and is 0"
more = f"Last digit of {number} is {last_digit} and is greater than 5"

if last_digit == 0:
    print(is_zero)
elif last_digit < 6 and last_digit > 0:
    print(less)
else:
    print(more)