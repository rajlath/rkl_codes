
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import Counter

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

valid = ["xx.", "x.x",".xx"]
def is_valid(mat):
    for i in mat:
        curr = "".join(i)
        for j in valid:
            if j in curr:
                return True
    return False


nb_test = int(input())

for _ in range(nb_test):
    ans = "NO"
    matrix = [[x for x in input()] for _ in range(4)]
    matcol = list(zip(*matrix))
    diagL = "".join([ matrix[i][i] for i in range(4) ])
    diagE = "".join([ row[-i-1] for i,row in enumerate(matrix) ])
    diag1, diag2 = [], []
    for j in range(4):
        diag2.append("".join([ row[i+j] for i,row in enumerate(matrix) if 0 <= i+j < len(row)]))
    print(diag)
    if is_valid(matrix):
        ans = "YES"
    elif is_valid(matcol):
        ans = "YES"
    for i in valid:
         if i in diagL or i in diagE:
             ans = "YES"
             break
    print(ans)













