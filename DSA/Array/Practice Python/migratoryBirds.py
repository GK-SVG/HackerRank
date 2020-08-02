#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    temp=arr
    tcount=0
    maximum=0
    num=0
    tarr=set(arr)
    for i in tarr:
        tcount=temp.count(i)
        if tcount>maximum:
            num=i
            maximum=tcount
    return num
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
