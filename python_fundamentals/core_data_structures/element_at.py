#!/usr/bin/env python3
def element_at(my_list, idx):
    num_of_elem = len(my_list)
    if idx < 0 or idx > num_of_elem - 1:
        return None
    else:
        elem = my_list[idx]
        return elem
