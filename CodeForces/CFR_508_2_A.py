from string import ascii_uppercase as uc
from collections import Counter
n, k = [int(x) for x in input().split()]
valids = uc[:k]
ins  = Counter(input())
val  = sorted(ins.values())[0]
print(val * k)
