#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    result = 0
    n = len(matrix) // 2
    # Iterate over the n x n top-left quadrant
    for i in range(n):
        for j in range(n):
            # For each position (i, j), consider the 4 possible positions
            top_left = matrix[i][j]
            top_right = matrix[i][2*n - 1 - j]
            bottom_left = matrix[2*n - 1 - i][j]
            bottom_right = matrix[2*n - 1 - i][2*n - 1 - j]
            # Take the maximum of the four possible flips
            result += max(top_left, top_right, bottom_left, bottom_right)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
