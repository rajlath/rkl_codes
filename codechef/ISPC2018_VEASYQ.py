
# -*- coding: utf-8 -*-
# @Date    : 2018-11-28 09:53:46
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



# -*- coding: utf-8 -*-
# @Date    : 2018-11-28 10:04:01
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

def add(arr, N, lo, hi, val):
    arr[lo] += val
    if (hi != N - 1):
        arr[hi+1] -= val
    return arr

def updateArray(arr, N)        :
    for i in range(1, N):
        arr[i] += arr[i-1]
    return arr

nb_students = read_int()
nb_professors = read_int()
arr = [0] * nb_students
for _ in range(nb_professors):
    val, l, r = read_ints()
    arr = add(arr,nb_students, l-1, r-1, val )
arr = updateArray(arr, nb_students)
maxs = max(arr)
indx = 0
ans  = []
for i in arr:
    indx += 1
    if i == maxs:
        ans.append(indx)
print(len(ans))
print(*ans)



