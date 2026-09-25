#!/usr/bin/env python3
for i in range(97, 123):
    # ASCII value for lowercase range a-z
    if i != 101 and i != 113:
        # ASCII value for q and e
        print("{}{}".format(chr(i), "\n" if i == 122 else ""), end="")
        # 1st {} gets chr(i) - 2nd {} gets the \n or empty string
