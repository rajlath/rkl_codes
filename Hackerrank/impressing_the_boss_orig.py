#!/bin/python3

import os
import sys

#
# Complete the canModify function below.
#
def canModify(a, n):
    for i in range(n):
        b = a[:i] + a[(i+1):]
        print(b)
        correct = True
        for j in range(n-2):
            if b[j] > b[j+1]:
                correct = False
                break
        if correct:
            return "YES"
    return "NO"
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for case in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canModify(a, n)
        print(result)
        #fptr.write(result + '\n')

    #fptr.close()