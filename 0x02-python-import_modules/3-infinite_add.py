#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    args = argv[1:]
    result = sum(map(int, args))

    print(result)
