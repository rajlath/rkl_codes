from math import gcd
def agcd(arr):
    rets = arr[0]
    for i in arr:
        rets = gcd(i, rets)
    return rets

n = int(input())
a = [int(x) for x in input().split()]
m = max(a)
b = [m - i for i in a]
g = agcd(b)
s = sum([i//g for i in b])
print(s, g)
