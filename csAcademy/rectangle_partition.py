
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 16:14:18
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

height, width, vertical, horizental = read_ints()
vertical_lines   = sorted([0] + read_ints() + [vertical+1])
horizental_lines = sorted([0] + read_ints() + [horizental+1])
vertical_lens, horizental_lens = [0] * int(100001), [0] * int(100001)
for i in range(1, vertical+1):
    vertical_lens[vertical_lines[i] - vertical_lines[i-1]] += 1
for i in range(1, horizental + 1):
    horizental_lens[horizental_lines[i] - horizental_lines[i-1]] += 1
ans = 0
for i in range(1, int(1e5)):
    ans += 1 * vertical_lens[i] * horizental_lens[i]
print(ans)



