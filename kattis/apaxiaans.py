from itertools import groupby
ins = groupby(input())
for k, g in ins:
    print(k, end='')