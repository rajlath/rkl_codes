
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

nb_songs, total_time = read_ints()
song_length = read_ints()
time_for_jokes = total_time - sum(song_length)
if time_for_jokes >= (nb_songs - 1) * 10:
    print(time_for_jokes//5)
else:
    print(-1)

