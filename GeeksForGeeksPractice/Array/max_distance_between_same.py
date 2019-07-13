'''
Given an array with repeated elements, the task is to find the maximum distance between two occurrences of an element.


Input:

The first line of input will contain no of test cases T . Then T test cases follow . Each test case contains 2 lines. The first line of each test case contains an integer N denoting the number of elements in the array, the next line contains N space separated integer's.


Output:

For each test case in new line print the Maximum distance between two occurrences of an element


Constraints:

1<=T<=100

1<=N<=1000


Example:

Input

2
6
1 1 2 2 2 1
12
3 2 1 2 1 4 5 8 6 7 4 2

Output

5
10

Explanation

Test case 1:
arr[] = {1, 1, 2, 2, 2, 1}
Max Distance: 5
Distance for 1 is: 5-0 = 5
Distance for 2 is : 4-2 = 2
Max Distance 5

Test case 2:
arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}
Max Distance 10
maximum distance for 2 is 11-1 = 10
maximum distance for 1 is 4-2 = 2
maximum distance for 4 is 10-5 = 5

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
'''


# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 17:58:41
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


def maxDistance(arr, n):
    dicts = {}
    distance = 0
    for i in range(n):
        if arr[i] in dicts:
            distance = max(distance, i - dicts[arr[i]])
        else:
            dicts[arr[i]] = i
    return distance
print(maxDistance([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2], 12))
