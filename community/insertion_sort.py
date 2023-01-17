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
    length = n
    current = arr[length-1]
    for i,num in enumerate( arr[::-1]):
        
        if current<num:
            arr[length-i]=arr[length-i-1]
            # print(arr)
            listToStr = ' '.join(map(str, arr))
            print(listToStr)
            if length-i==1:
                arr[length-i-1]= current
                listToStr = ' '.join(map(str, arr))
                print(listToStr)
                
        elif current>num:
            arr[length-i]=current
            # print(arr)
            listToStr = ' '.join(map(str, arr))
            print(listToStr)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
