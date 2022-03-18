#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    myStack=[]
    # Write your code here
    for i in range(len(grades)):
        rounded=round(grades[i]/5)*5 #since number is integer
        if grades[i]<38:
            myStack.append(grades[i])
        elif grades[i]<rounded:
            myStack.append(rounded)
        else:
            myStack.append(grades[i])
    return myStack
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
