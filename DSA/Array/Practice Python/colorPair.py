#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count=1
    count2=0
    temparr=[]
    tempAr=sorted(ar)
    tempAr.append(0)
    for i in range(n):
        if tempAr[i]==tempAr[i+1]:
            count+=1
        else:
            temparr.append(count)
            count=1
    for i in range(len(temparr)):
        count2+=int(temparr[i]/2)
    return count2


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    
