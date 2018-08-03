from itertools import groupby
noc, x, y = [int(x) for x in input().split()]
s = input()
sg = groupby(s)
sg = [(k, list(g)) for k, g in sg if set(list(g)) == {"0"}]
lsg = len(sg)
ans = ((len(sg) - 1) * min(x, y) + y)
print(0 if lsg ==0 else ans)
'''
zeros = []
for k, v in sg:

    if set(v) == {"0"}:
        zeros.append(v)
if len(zeros) == 0:
    print(0)
else:
    print( (len(zeros)-1) * min(x, y) + y)
'''