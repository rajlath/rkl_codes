from math import gcd

l, r, x, y = [int(x) for x in input().split()]
vals = x * y
hashset = set()
cnt = 0
for i in range(l, r+1):
    if vals % i == 0 and gcd(i, vals//i)==x:
        cnt += 1
print(cnt)