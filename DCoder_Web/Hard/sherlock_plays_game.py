'''
Problem statement
Sherlock and Watson just got off a crime case and were really bored. They decided to play a board game which given to them by a former client of theirs. The game is called "The Great Game". The Great Game starts by writing an array that is given on the board. Sherlock and Watson take turns by removing exactly one number from the array, Sherlock takes first turn, obviously.
Following are the rules :-
1. If at any point of the game, removing a number causes the XOR-ALL(bitwise XOR of the entire array) to be 0, the player loses.
2. Bitwise XOR of one number is that number itself.
3. If any player starts their turn with XOR-ALL equal to 0, that player wins.

Assume that both Sherlock and Watson play this game optimally. Given an array, print "Sherlock" if he wins, else print "Watson", without the double quotes.
Input
The first line contains T, the number of test cases.
Each test case contains 2 lines, the first line contains N, the number of elements in the array. The second line contains N space separated integers.
Output
For each test case, print the winner in a new line. If Sherlock wins, print "Sherlock" or if Watson wins, print "Watson".
Constraint
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000
0 ≤ A[i] ≤ 2^16
Sample Input
1
4
1 2 3 4
Sample Output
Sherlock
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 13:16:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nots = read_int()
for _ in range(nots):
    lens = read_int()
    arrs = read_ints()
    xors = arrs[0]
    for i in arrs[1:]:
        xors ^= i
    if xors == 0 or lens%2==0:
        print("Sherlock")
    else:
        print("Watson")




