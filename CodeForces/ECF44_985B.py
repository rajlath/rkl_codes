'''
author raju lath
Date   230520181202
link   http://codeforces.com/contest/985/problem/B
Examples
input
4 5
10101
01000
00111
10000
output
YES
input
4 5
10100
01000
00110
00101
output
NO
'''
n, m = [int(x) for x in input().split()]

lamps = []
cnt   = [0 for x in range(m)]
for _ in range(n):
    lamps.append([int(x) for x in input()])
for i in range(n):
    for j in range(m):
        if lamps[i][j] == 1: cnt[j]+=1
print(cnt)





