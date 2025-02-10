#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxElement' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER maxSum
#  3. INTEGER k
#
'''
ALL PASS, not my solution :(
'''

import math

def maxElement(n, maxSum, index):
    # Write your code here
    maxSum -= n
    if index < n // 2:
        index = n - index - 1
    n_left = index
    n_right = n - 1 - index
    tri_left = (n_left * (n_left + 1)) // 2
    tri_right = (n_right * (n_right + 1)) // 2
   
    if maxSum <= (tri_right * 2 + n_right + 1):
        return int(math.sqrt(maxSum)) + 1
    
    if maxSum <= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1):
        b = 3 + 2 * n_right
        return int((-b + math.sqrt(b * b - 8 * (tri_right + 1 - n_right * n_right - maxSum))) / 2) + 1 + 1
    
    maxSum -= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1)
    return n_left + 1 + 1 + (maxSum // n)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    fptr.write(str(result) + '\n')

    fptr.close()
