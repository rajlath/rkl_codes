n=input()
l=map(int, raw_input().split())
z=[0 for i in xrange(n+1)]
sol=[0 for i in xrange(n+1)]
for i in l:
	z[i]+=1
for i in xrange(n,0,-1):
	j=2
	g=z[i]
	sub=0
	while i*j<=n:
		g+=z[i*j]
		sub+=sol[i*j]
		j+=1
#	if sub==0:sub=1
	sol[i]=(pow(2, g, 1000000007) -1 - sub)%1000000007
for i in l:
	print sol[i],
print