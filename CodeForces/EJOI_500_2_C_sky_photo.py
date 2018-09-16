#-------------------------------------------------------------------------------
# Name:        EJOI_500_2_C_sky_photo.
# Purpose:     http://codeforces.com/contest/1013/problem/C
#
# Author:      rinfo
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n = int(input())
    a = [int(i) for i in input().split()]

    a.sort()

    x = a[n - 1] - a[0]
    y = a[2 * n - 1] - a[n]

    c1 = x * y

    x = a[2 * n - 1] - a[0]

    for i in range(1, n):
        c1 = min(c1, x * (a[i + n - 1] - a[i]))
    print(c1)

if __name__ == '__main__':
    main()
