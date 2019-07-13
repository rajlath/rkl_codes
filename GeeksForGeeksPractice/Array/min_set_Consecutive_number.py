'''
Given a word S and a text C. Return the count of the occurences of anagrams of the word in the text.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a text S consisting of only lowercase characters.
The second line contains a word consisting of only lowercase characters.

Output:
Print the count of the occurences of anagrams of the word C in the text S.

Constraints:
1 <= T <= 50
1 <= |S| <= |C| <= 50

Example:
Input:
2
forxxorfxdofr
for
aabaabaa
aaba

Output:
3
4

Explaination:
for, orf and ofr appears in the first test case and hence answer is 3.

'''


# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 19:24:17
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
    ins = input()
    looking_for = sorted(input())
    lins = len(ins)
    llook= len(looking_for)
    counts = 0
    for i in range(0, lins - llook + 1, 1):
        if sorted(ins[i:i+llook]) == looking_for:
            counts += 1
    print(counts)