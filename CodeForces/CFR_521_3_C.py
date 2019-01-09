
# -*- coding: utf-8 -*-
# @Date    : 2018-11-16 20:33:44
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


lens = read_int()
arrs = read_ints()
sums = sum(arrs)
ans  = []
valid = []
for i in range(len(arrs)):
    if arrs[i]  in valid:
        ans.append(i+1)
    else:
        curr = sums - arrs[i]
        if curr % 2 == 0 and  curr//2 in arrs and curr//2 != arrs[i]:
            ans.append(i+1)
            valid.append(arrs[i])

if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(*ans)
