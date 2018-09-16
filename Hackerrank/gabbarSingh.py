n=int(input());g,b=[],[]
for _ in range(n):
    i,j = map(int,input().split())
    if i==0:g.append(j)
    else: b.append(j)
print(*sorted(g,reverse=True),*sorted(b,reverse=True))


