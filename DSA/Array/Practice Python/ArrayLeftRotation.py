#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n=len(a)
    mod=d%n
    arr=[0]*n
    for i in range(n):
        t=(mod+i)%n
        arr[i]=a[t]
    return arr
    # for i in range(d):
    #     temp=a[0]
    #     for i in range(1,len(a)):
    #         a[i-1]=a[i]
    #     a[len(a)-1]=temp
    # return a


if __name__ == '__main__':
    
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
