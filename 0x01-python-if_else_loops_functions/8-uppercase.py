#!/usr/bin/python3

def uppercase(str):

    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            uppercase = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase = char
        result += uppercase

    print(result)
