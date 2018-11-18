#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
   # print(ar)
    sum = 0
    n=len(ar)
    print(n)
    for x in range(0,n):
        sum = sum+ar[x]
    print(sum)
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    #print(ar)

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
