#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    temp=[]
    maximumA=max(a)
    if maximumA>1:
        limit=(maximumA*10+1)
    else:
        limit=max(b)+1
    for i in range(maximumA,limit):
        count=0
        for j in range(len(a)):
            if i%a[j]==0:
                count+=1
        if count==len(a):
            temp.append(i)
    count2=0
    print(temp)
    for i in range(len(temp)):
        count=0
        for j in range(len(b)):
            if b[j]%temp[i]==0:
                count+=1
        if count==len(b):
            count2+=1
    return count2
    # Write your code here

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
