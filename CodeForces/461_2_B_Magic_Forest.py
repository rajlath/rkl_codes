#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      rinfo
#
# Created:     31/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n = int(input())
    cnt = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = a ^ b
            #print(a, b, c)
            if b <= c <= n and a + b > c:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
