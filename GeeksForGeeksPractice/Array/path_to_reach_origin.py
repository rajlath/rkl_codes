'''
You are standing on a point (n, m) and you want to go to origin (0, 0)
by taking steps either left or down i.e. from each point you are allowed
to move either in (n-1, m) or (n, m-1).
Find the number of paths from point to origin.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow.
Each test case contains two integers n and m representing the point.

Output:
For each testcase, in a new line, print the total number of paths from point to origin.

Constraints:
1 <= T<= 100
1 <= n, m <= 25

Example:
Input:
3
3 2
3 6
3 0

Output:
10
84
1

'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 19:10:51
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

def count_paths(n, m):
    if n == 0 or m == 0:return 1
    return count_paths(n-1, m) + count_paths(n, m-1)

nb_test = RI()
for _ in range(nb_test):
    n, m = RMI()
    print(count_paths(n, m))


