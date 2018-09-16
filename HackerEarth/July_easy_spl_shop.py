#-------------------------------------------------------------------------------
# Name:        July_circuit_18_special_shop
# Purpose:     https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/
#
# Author:      rinfo
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import ceil, floor
def main():
    for _ in range(int(input())):
        n, a, b = [int(x) for x in input().split()]
        r =(n * b) / (a + b)
        if ceil(r) - r <= r - floor(r):
            r = ceil(r)
        else:
            r = floor(r)
        rb = n - r
        ans = (r * r * a)  + (rb * rb *b)
        print(ans)



if __name__ == '__main__':
    main()
