'''
Given a array a[] of non-negative integers. Count the number of pairs (i, j) in the array such that a[i] + a[j] < a[i]*a[j]. (the pair (i, j) and (j, i) are considered same and i should not be equal to j)

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. The next line contains n space separated integers respectively forming the array.

Output:
Print the total number of pairs possible in the array according to the problem statement.

Constraints:
1<=T<=10^5
1<=n<=10^5
1<=a[i]<=10^5

Example:
Input:
2
3
3 4 5
3
1 1 1

Output:
3
0
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 18:19:45
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    arrs = RMI()
    done = set()
    counts = 0
    for i in range(lens):
        for j in range(lens):
            if i != j and (i, j) not in done and (j, i) not in done:
                if arrs[i] + arrs[j] < arrs[i] * arrs[j]:
                    done.add((i, j))
    print(len(done))