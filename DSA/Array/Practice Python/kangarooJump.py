#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    count1=0
    count2=0
    while count1!=count2 or x1!=x2:
        if x1<=10000000 and x2<=10000000:
            x1+=v1
            x2+=v2
            count1+=1
            count2+=1
        else:
            print('x1==',x1,'x2==',x2,'count1==',count1,'count2==',count2)
            return 'NO'
    print('x1==',x1,'x2==',x2,'count1==',count1,'count2==',count2)
    return 'YES'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)


    # fptr.write(result + '\n')

    # fptr.close()
