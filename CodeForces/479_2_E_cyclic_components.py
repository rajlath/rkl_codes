n,m=map(int,input().split())
b=[[] for i in range(n+1)]
for i in range(m):
    c,d=map(int,input().split())
    b[c].append(d);b[d].append(c)
cands = set(i for i in range(n+1) if len(b[i]) == 2)
res = 0
while cands:
	v = cands.pop()
	R, L = b[v]
	while L in cands:
		cands.remove(L)
		V1, V2 = b[L]
		if V1 in cands:
			L = V1
		elif V2 in cands:
			L = V2
		else:
			break
		if L == R:
			res += 1
print (res)