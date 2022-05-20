

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    seeLevel=0
    count=0
    for i in path:
        if(i=="U"):
            seeLevel+=1
            if (seeLevel==0):
                count+=1
        else:
            seeLevel-=1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
