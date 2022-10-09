#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    pos = len(arr) - 1
    for col, col_val in enumerate(arr):
        for row, row_val in enumerate(col_val):
            if col == row:
                left_diagonal += arr[col][row]
            if pos == row:
                right_diagonal += arr[col][row]
        pos -= 1

    return abs(left_diagonal - right_diagonal)


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
