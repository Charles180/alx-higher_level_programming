#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    tail_num = number % 10
    print(tail_num, end='')
    return tail_num
