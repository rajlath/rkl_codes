#-------------------------------------------------------------------------------
# Name:        COLCHEF
# Purpose:     https://www.codechef.com/LOCJUL18/problems/COLCHEF  #
# Author:      oorjaHalt_rinfo_raj                                 #
# Created:     31/07/2018
# Copyright:   (c) rinfo 2018
# Python   :   Python3.6
#-------------------------------------------------------------------------------
#CodeChef submission 19394239 (C) plaintext list. Status: AC,
#problem COLCHEF, contest LOCJUL18. By devendraraj (devendraraj),
#2018-07-29 22:04:00.
#Translated to python3 by me.
def main():
    nos = int(input())
    noq = int(input())
    a = [i for i in range(nos+1)]
    maxs= int(10e12)

    for _ in range(noq):
        c, x, y = [int(x) for x in input().split()]
        if c is 0:
            if a[y] is y and a[x] is x :
                a[x] += maxs
                a[y]  = a[x]
            elif a[y] is y and a[x] is not x:
                a[y] = a[x]
            elif a[y] is not y and a[x] is x:
                a[x] = a[y]
            elif a[y] is not y and a[x] is not x:
                s, p = a[y], a[x]
                for i in range(1, nos+1):
                    if a[i] is s:a[i] = p
        elif c is 1:
            if a[x] == a[y] : print("YES")
            else:print("NO")


if __name__ == '__main__':
    main()
