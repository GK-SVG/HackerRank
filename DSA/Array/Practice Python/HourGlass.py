#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    li=[]
    for i in range(4):
        for j in range(4):
            count=0
            add=0
            for k in range(j,j+3):
                add+=arr[i][k]+arr[i+2][k]
                count+=1
                if count==2:
                    add+=arr[i+1][k]

            li.append(add)
    return max(li)
            

            

if __name__ == '__main__':
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)