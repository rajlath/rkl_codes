'''
Write a program to find the sum of bit differences in all pairs that can be formed
from array elements n. Bit difference of a pair (x, y) is a count of different bits
at same positions in binary representations of x and y.
For example, bit difference for 2 and 7 is 2.
Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).

Input: The first line of input contains an integer T denoting the number of test cases.
       First line of the test case will contain an array of elements n.

Output: The sum of bit differences of all pairs that can be formed by given array.

Constraints:

1 <=T<= 100

1 <=N<= 10

1 <=a[i]<= 10
Example:

Input:

2
2
1 2
3
1 3 5

Output:

4
8
'''



# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 17:40:15
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


# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 17:12:09
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0


def sum_of_bit_difference(arr, N):
    rets = 0
    for i in range(32):
        count= 0
        for j in range(N):
            if arr[j] & (1 << i):count += 1
        rets += (count * (N - count) * 2)
    return rets

nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    arrs = RMI()
    print(sum_of_bit_difference(arrs, lens))
