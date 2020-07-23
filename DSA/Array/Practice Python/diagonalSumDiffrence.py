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
    # Write your code here
    n=len(arr)
    count=0
    dia1=0
    dia2=0
    while(count<n):
        dia1+=arr[count][count]
        count+=1
    count=0
    n-=1
    while(n>=0):
        dia2+=arr[count][n]
        count+=1
        n-=1

    if dia1-dia2<0:
        return (-1)*(dia1-dia2)
    else:
        return dia1-dia2


if __name__ == '__main__':
    
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
