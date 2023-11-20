#!/usr/bin/python3
def safe_print_list(my_list=[], c=0):
    try:
        for x in range(c):
            print(my_list[x], end="")
    except IndexError:
        c = x
    finally:
        print()
        return c
