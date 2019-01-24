
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 12:24:28
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


ans = "YES"
for i in range(3):
    curr = input()
    print(curr)
    count= sum([1 for x in curr if x in 'aeiou'])
    #print(count)
    if (i in [0,2] and count == 5) or (i == 1 and count == 7):
        continue
    else:
        ans = "NO"
        break
print(ans)

print('YES' if [sum(1 for ch in input() if ch in {'a', 'e', 'i', 'o', 'u'}) for i in range(3)] == [5, 7, 5] else 'NO')

