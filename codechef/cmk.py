#-------------------------------------------------------------------------------
# Name:        CMK
# Purpose:     https://www.codechef.com/LOCJUL18/problems/CMK
#
# Author:      rinfo
#
# Created:     31/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    for _ in range(int(input())):
        n, k = [int(x) for x in input().split()]
        a    = [int(x) for x in input().split()]
        b    = [int(x) for x in input().split()]
        asort= sorted(a)
        bsort= sorted(sorted(b, reverse=True)[:k])
        c  = 0
        for i in range(k):
            if bsort[i] > asort[i]:c += 1
        print(["NO", "YES"][c >= k])

if __name__ == '__main__':
    main()
