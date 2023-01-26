#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    last=" ".join(map(str,arr))
    for i in range(n-1,-1,-1):
        temp=i
        for j in range(i,-1,-1):
            if arr[j]>=arr[temp]:
                temp=j
        a=arr[i]
        arr[i]=arr[temp]
        if last !=' '.join(map(str, arr)):
            print(' '.join(map(str, arr)))
        last=' '.join(map(str, arr))
        arr[temp]=a

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
