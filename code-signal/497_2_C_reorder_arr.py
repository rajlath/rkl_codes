from collections import Counter
n = int(input())
a = Counter([int(x) for x in input().split()])
print( n - max(a.values()))
