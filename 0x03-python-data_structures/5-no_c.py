#!/usr/bin/python3

def no_c(my_string):
    cees = {'c', 'C'}

    new = ''.join(char for char in my_string if char.lower() not in cees)

    return new
