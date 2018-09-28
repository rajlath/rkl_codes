
# -*- coding: utf-8 -*-
# @Date    : 2018-09-28 09:18:53
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

nb_rows = read_int()
done = False
answer = []
for i in range(nb_rows):
    seats = input().split("|")
    for i,v in enumerate(seats):
        if v == "OO" and not done:
            seats[i] = "++"
            done = True
        else:
            seats[i]= v
    answer.append("|".join(seats))
if done:
    print("YES")
    print("\n".join(answer))
else:
    print("NO")



