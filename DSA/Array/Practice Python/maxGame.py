#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    count=0
    while(s-p>0):
        s-=p
        count+=1
        if p-d>m:
            p-=d
        else:
            p=m
    return count

    # Return the number of games you can buy

if __name__ == '__main__':

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
