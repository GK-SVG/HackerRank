#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    li=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                temp=j-i
                li.append(temp)
                break
    minimum=min(li)
    return minimum

        

if __name__ == '__main__':
    
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)

    
