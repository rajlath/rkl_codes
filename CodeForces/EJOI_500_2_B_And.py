#-------------------------------------------------------------------------------
# Name:        EJOI_500_2_B_AND
# Purpose:
#
# Author:      rinfo
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n, x = [int(x) for x in input().split()]
    a  = set([int(x) for x in input().split()])
    if len(a) != n: ans = 0
    else:
        offsets = set()
        ans = -1
        for i in a:
            curr = i & x
            offsets.add(curr)
            if curr in a and curr != i:
                ans = 1
        if len(offsets) != n and ans == -1:
            ans = 2
    print(ans)




if __name__ == '__main__':
    main()
