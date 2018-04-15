#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    i = 0
    sums = 0

    while True:
        ax = [int(10e12), a[0]][len(a)>0]
        bx = [int(10e12), b[0]][len(b)>0]

        if ax < bx:
            a.pop(0)
            sums += ax
            if sums > x:return i
            i += 1
        elif bx < ax:
            b.pop(0)
            sums += bx
            if sums > x:return i
            i += 1
        elif ax == bx:
            if ax == int(10e12):
                return -1
            else:
                a.pop(0)
                sums += ax
                if sums > x: return i
                i += 1


if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        print(str(result) + '\n')

