#-------------------------------------------------------------------------------
# Name:        cave painting
# Purpose:
#
# Author:      rinfo
#
# Created:     31/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n, k  = [int(x) for x in input().split()]
    x = 1
    ans = "YES"
    while x <= k:
        if n % x != x - 1 :
            ans ="NO"
            break
        x += 1
    print(ans)


if __name__ == '__main__':
    main()
