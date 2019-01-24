
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 09:38:59
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

lens = int(input())
genome= input()
counts = [genome.count(i) for i in "ACGT"]
ans = "==="
if lens%4==0 and max(counts) <= lens//4:
    ans = ''
    i = 0
    for x in genome:
        if x == "?":
            while i < 4 and counts[i]>=lens//4:
                i += 1
            ans += 'ACGT'[i]
            counts[i]+= 1
        else:
            ans += x
print(ans)





