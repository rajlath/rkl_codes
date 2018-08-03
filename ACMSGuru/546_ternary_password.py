'''
sample input
sample output
6 1 3
012022
2
111022

sample input
sample output
5 5 0
02211
4
00000
'''
lens, zeros, ones = [int(x) for x in input().split()]
s = input()
if lens < (zeros + ones):
    print("-1")
else:

    twos = lens - (zeros + ones)
    t    = "0" * zeros + "1" * ones + "2" * twos
    s = sorted(s)
    cnt = 0
    for (a, b) in zip(s, t):
        if a != b:cnt += 1
    print(cnt)
