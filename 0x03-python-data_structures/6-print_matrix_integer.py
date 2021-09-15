#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 1
    for idx in matrix:
        for i in idx:
            if x < len(idx):
                print("{}".format(i), end=" ")
                x += 1
            else:
                print("{}".format(i))
                x = 1
    if matrix == [[]]:
        print()
