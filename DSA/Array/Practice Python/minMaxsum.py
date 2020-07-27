#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max=0
    min=0
    temp=0
    for i in range(len(arr)):
        temp=sum(arr)-arr[i]
        if temp>max:
            max=temp
        if temp<min:
            min=temp
    print(f'{min} {max}')





if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
