#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus=0
    minus=0
    zero=0
    for i in range(len(arr)):
        if arr[i]<0:
            minus+=1
        elif arr[i]==0:
            zero+=1
        else:
            plus+=1
    print('%.6f'%(plus/len(arr)))
    print('%.6f'%(minus/len(arr)))
    print('%.6f'%(zero/len(arr)))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
