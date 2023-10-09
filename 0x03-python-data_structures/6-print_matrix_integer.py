#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for new_matrix, value in enumerate(row):
            if new_matrix != len(row) - 1:
                print("{:d}".format(value), end=" ")

            else:
                print("{:d}".format(value))

    print()
