
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 12:44:17
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


nb_tracks , dest = read_ints()
dest -= 1
track_up = read_ints()
track_dn = read_ints()
ans = "NO"
if not track_up[0]:
    ans = "NO"
elif track_up[dest]:
    ans = "YES"
else:
    if any(track_up[i] and track_dn[i] and track_dn[dest] for i in range(dest, nb_tracks)):
        ans = "YES"
print(ans)

