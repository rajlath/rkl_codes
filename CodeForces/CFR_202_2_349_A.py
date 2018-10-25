
# -*- coding: utf-8 -*-
# @Date    : 2018-10-02 08:00:37
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


nb_people = read_int()
have = read_ints()
_25 = 0
_50 = 0
can = "YES"
for has in have:
    if has == 25: _25 += 1
    elif has == 50:
        _50 += 1
        _25 -= 1
    else:
        if _50 > 0:
            _50 -= 1
        else:
            _25 -= 2
        _25 -= 1
    if _25 < 0 or _50 < 0:
        can = "NO"
        break
print(can)

