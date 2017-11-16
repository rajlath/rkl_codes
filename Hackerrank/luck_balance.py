'''
6 3
5 1
2 1
1 1
8 1
10 0
5 0
'''
noc , k = [int(x) for x in input().split()]
imp, nimp = [], []
for i in range(noc):
    l, im = [int(x) for x in input().split()]
    if im == 0: nimp.append(l)
    else: imp.append(l)
imps = sorted(imp, reverse= True)

ans  = sum(imps[:k]) - sum(imps[k:]) + sum(nimp)
print(ans)
