mod = 1000000007

nb = int(input())
ar = sorted([int(x) for x in input().split()])
while len(ar) > 1:
    ar.append((ar.pop() * ar.pop()) % mod)
print(ar[0])
