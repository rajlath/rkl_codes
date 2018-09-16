#-------------------------------------------------------------------------------
# Name:        LOCJUL18_CMK
# Purpose:     https://www.codechef.com/LOCJUL18/problems/CMK
#
# Author:      oorja_rinfo_raj
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    for _ in range(int(input())):
        nows, k = [int(x) for x in input().split()]
        opps    = [int(x) for x in input().split()]
        chef    = [int(x) for x in input().split()]
        oppss   = sorted(opps)
        chefs   = sorted(chef, reverse=True)[:k]
        chefs   = sorted(chefs)
        valid   = sum([1 for x in range(k) if chefs[x] > oppss[x]])
        print(["NO", "YES"][valid >= k])



if __name__ == '__main__':
    main()
