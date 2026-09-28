#!/usr/bin/env python3
def replace_in_list(my_list, idx, element):
    num_elem = len(my_list)
    if idx < 0 or idx > num_elem - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
