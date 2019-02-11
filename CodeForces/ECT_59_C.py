from itertools import groupby
lens , k = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]
ins = input()
insg = [len(list(g)) for k, g in groupby(ins)]
i = 0
ans = 0
for x in insg:
    ans += sum(sorted(vals[i:i+x], reverse=True)[:k])
    i += x
print(ans)




