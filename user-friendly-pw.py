#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def authEvents(events):
    M = pow(10,9) + 7
    p = 131
    
    def calc(data):
        ans = 0
        for i, num in enumerate(reversed(data)):
            ans += ord(num)*pow(p,i,M)%M
        return ans%M
    
    ans = []
    for event,data in events:
        if event == 'setPassword':
            db = set()
            og = calc(str(data))
            db.add(str(og))
            og = og*p%M
            for i in range(48,58):
                db.add(str((og + i)%M))
            for i in range(65,91):
                db.add(str((og+i)%M))
            for i in range(97,123):
                db.add(str((og+i)%M))
        
        elif event == 'authorize':
            if data in db:
                ans.append(1)
            else:
                ans.append(0)
    return ans
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
