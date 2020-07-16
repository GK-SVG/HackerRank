#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num=int(n/len(s))
    reminder=n%len(s)
    count=0
    for i in range(len(s)):
        if s[i]=='a':
            count+=1
    count2=count*num
    count=0
    for i in range(reminder):
        if s[i]=='a':
            count+=1
    count2+=count

    return count2


    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
