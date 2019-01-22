
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

def get_count(n):
    segment=[6,2,5,5,4,5,6,3,7,6]
    ns = str(n)
    count = 0
    for i in ns:
        count += segment[int(i)]
    return count


nb_on = {0:6, 1:2, 2:4, 3:6, 4:4, 5:5, 6:5, 7:3, 8:7, 9:6}

nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    elem = read_ints()


mins = int(10e10)
for i in elem:
    curr = get_count(i)
    if curr < mins:
        ans = i
        mins= curr
print(ans)



