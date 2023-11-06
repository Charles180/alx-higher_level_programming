#!/usr/bin/python3
def element_at(my_list, x):
    if x < 0 or x > len(my_list) - 1:
        return 'None'
    else:
        return my_list[x]
