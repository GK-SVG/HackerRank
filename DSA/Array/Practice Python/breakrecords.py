#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max=scores[0]
    min=scores[0]
    count1=0
    count2=0
    for i in range(len(scores)):
        if scores[i]<min:
            min=scores[i]
            count1+=1
        if scores[i]>max:
            max=scores[i]
            count2+=1

    return [count2,count1]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
