#!/usr/bin/env python3
def uppercase(str):
    string_to_print = ""
    for letter in str:
        char_to_ascii = ord(letter)
        if 97 <= char_to_ascii <= 122:  # if the character is a lowercase
            char_to_ascii = char_to_ascii - 32  # convert to uppercase
            letter = chr(char_to_ascii)  # convert from ASCII back to letter
            string_to_print += letter  # append
        else:
            string_to_print += letter
    print(string_to_print)
