#!/usr/bin/env python3
letters_to_print = ""
# for every character in the string that I gave
for char in "abcdefghijklmnopqrstuvwxyz":
    # if the character is not q and is not e
    if char != "q" and char != "e":
        # append the letter into letters to print
        letters_to_print += char

print(letters_to_print)
