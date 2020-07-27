#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:]=='PM':
        s=str(int(s[:2])+12)+s[2:]
    elif s[-2:]=='AM' and s[:2]=='12':
         s=(str(int(s[:2])-12))*2+s[2:]
    return s[:-2]

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
