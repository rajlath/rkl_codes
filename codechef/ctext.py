
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 19:05:36
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

slh = ["abcdefghijklm", "nopqrstuvwxyz"]
sl2 = ["nopqrstuvwxyz", "abcdefghijklm"]
clh = ["ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"]
cl2 = [ "NOPQRSTUVWXYZ","ABCDEFGHIJKLM"]
dg1 = ["01234", "56789"]
dg2 = ["56789", "01234"]

nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())

    ins  = input()
    ans  = ''

    for i in ins:

        if   i in slh[0]:ans += slh[1][slh[0].index(i)]
        elif i in sl2[0]:ans += sl2[1][sl2[0].index(i)]
        elif i in clh[0]:ans += clh[1][clh[0].index(i)]
        elif i in cl2[0]:ans += cl2[1][cl2[0].index(i)]
        elif i in dg1[0]:ans += dg1[1][dg1[0].index(i)]
        elif i in dg2[0]:ans += dg2[1][dg2[0].index(i)]
        else:ans += i
    print(ans)
