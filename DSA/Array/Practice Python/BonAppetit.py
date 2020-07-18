import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total=sum(bill)
    print('total==',total)
    total-=bill[k]
    print('total==',total)
    actual=int(total/2)
    if actual==b:
        print('Bon Appetit')
    else:
        print(b-actual)



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
