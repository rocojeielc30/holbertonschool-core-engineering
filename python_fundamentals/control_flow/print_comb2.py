#!/usr/bin/env python3
for number in range(99):
    print("{:02d}{}".format(number, ", " if number < 98 else "\n"), end="")
