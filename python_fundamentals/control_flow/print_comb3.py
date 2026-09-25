#!/usr/bin/env python3
for number in range(10):
    tens_digit = number
    for number in range(number+1, 10):
        ones_digit = number
        print("{}{}".format(tens_digit, ones_digit),
              end="\n" if tens_digit == 8 and ones_digit == 9 else ", ")
