#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#
'''
11/15 PASS
'''
def stockPairs(stocksProfit, target):
    # Write your code here
    nums = {}
    matches = 0
    for i in stocksProfit:
        if i not in nums:
            nums[i] = 1 # Track which elements are already used
            for x in nums:
                if x != i and x + i == target:
                    matches += 1
    return matches
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(input().strip())

    stocksProfit = []

    for _ in range(stocksProfit_count):
        stocksProfit_item = int(input().strip())
        stocksProfit.append(stocksProfit_item)

    target = int(input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()
