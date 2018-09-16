#-------------------------------------------------------------------------------
# Name:        EJOI_500_2_A_piles
# Purpose:     http://codeforces.com/contest/1013/problem/A
#
# Author:      rinfo
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
Examples
inputCopy
5
1 2 3 4 5
2 1 4 3 5
outputCopy
Yes
inputCopy
5
1 1 1 1 1
1 0 1 0 1
outputCopy
Yes
inputCopy
3
2 3 9
1 7 9
outputCopy
No
'''
def main():
    n = int(input())
    day1 = [int(x) for x in input().split()]
    day2 = [int(x) for x in input().split()]
    movep = 0
    taken_or_moved = 0

    for i, v in enumerate(day1):
        if day2[i] > day1[i]:
            movep += day2[i] - day1[i]
        elif day2[i] < day1[i]:
            taken_or_moved += day1[i] - day2[i]
    print(["No", "Yes"][movep <= taken_or_moved])





if __name__ == '__main__':
    main()
