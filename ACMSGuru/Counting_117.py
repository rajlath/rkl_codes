from math import gcd

n, m, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

def isvalid(t, m, k):
    if m == 1 or t == 1:return t%k==0
    d = gcd(t, k)
    return isvalid(t, m-1, k//d)

cnt = 0
for i in range(n):
    cnt += isvalid(arr[i], m, k)
print(cnt)

