
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:29:00
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

rows, cols = read_ints()
matrix = []
for _ in range(rows):
    matrix.append(read_ints())
offsets = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
B = []
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        curr = [matrix[i+d[0]][j+d[1]] for d in offsets]
        B.append([sum(curr), i, j, curr])
B = sorted(B, reverse = True)
t = len(B)
maxi = -1
for i in range(len(B)):
    if B[i][0] * B[i][0] <= maxi: break
    i_max = max(B[i][3])
    for j in range(i+1, t):
        if i_max * B[j][0] <= maxi: break
        if abs(B[i][1] - B[j][1]) + abs(B[i][2] - B[j][2]) <= 1: continue
        val = sum([B[i][3][k] * B[j][3][k] for k in range(5)])
        if val > maxi: maxi = val

print(maxi)

