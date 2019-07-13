'''
You are given an array A[] , you have to construct a new array A2[].
The values in A2[] are obtained by doing Xor of consecutive elements in array.

Input:
First line of the input contains t, the number of test cases. Each line of the test case contains a number n specifying the number of elements.
Each 'n' lines denoting elements of array A[].

Output:
Each new line of the output contains element of array A2[] .



Constraints:

1<=t<=100

1<=n<=100000

1<=A[i]<=100000

Example:

Sample Input 0
1
5
10 11 1 2 3

Sample Output 0
1 10 3 1 3
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 10:57:52
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
    answer = [x ^ y for x, y in zip(arrs, arrs[1:])]
    answer +=[arrs[-1]]
    print(*answer)