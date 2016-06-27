# -*- coding: utf-8 -*-


# --------------First Method ---------------
def binary_gap(n):
    bin_value = bin(n).strip('0b').strip().split('1')
    temp = 0
    for value in bin_value:
        value_len = len(value)
        if value_len > temp:
            temp = value_len
    return temp

binary_gap(1025)


# --------------Second Method ---------------
def binary_gap(n):
    bin_value = bin(n).replace('0b', '').split('1')
    max_value = max(bin_value, key=lambda x: x)
    return len(max_value)

binary_gap(1025)