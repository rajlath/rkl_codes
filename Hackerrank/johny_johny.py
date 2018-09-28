
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 16:31:01
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

'''
2
5 3 3
baaab
4 3 3
abbb
'''

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_test = read_int()
for _ in range(nb_test):
    n, x, y = read_ints()
    s       = read_str()
    cnt_a = sum([1 for x1 in s if x1 == 'a'])
    cnt_b = n - cnt_a
    if (x + y ) != cnt_a * cnt_b:
        print("Impossible")
        continue

    else:
        print("Possible")
        ans = ''
        for i in range(n):
            tmp1 = cnt_b
            tmp2 = cnt_b * (cnt_a - 1)
            if tmp1 <= x and tmp2 >= y:
                ans += 'a'
                cnt_a -= 1
                x -= cnt_b
            else:
                cnt_b -= 1
                y -= cnt_a
                ans += 'b'
    print(ans)



