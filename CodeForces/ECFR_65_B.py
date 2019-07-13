import sys
import math
import itertools


def ask(l, r):
    print('?', l, r)
    sys.stdout.flush()
    n = int(input())
    return n


def answer(lst):
    print('!', *lst)


jury = [4, 8, 15, 16, 23, 42]
perm = list(itertools.permutations(jury))
ab = ask(1, 2)
bc = ask(2, 3)
cd = ask(3, 4)
de = ask(4, 5)
for a, b, c, d, e, f in perm:
    if a * b == ab and b * c == bc and c * d == cd and d * e == de:
        answer([a, b, c, d, e, f])