
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

nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    ins  = input()
    ans  = ins[0].upper()
    last  = ''
    vowel = 'aeiou'
    clen = 0
    for i in ins[1:]:
        if i in vowel:
            if clen != 0:
                ans += str(clen)
                clen = 0
                last = ''
            if i == last:
                continue
            else:
                ans += i
            last = i
        else:
            clen += 1
    if clen > 0: ans += str(clen)
    print(ans)








