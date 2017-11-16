I = lambda:map(int, input().split())
n, k, m = I()
b = [[] for i in range(m)]
for x in I():
	b[x % m].append(x)
print(b)    
for i in range(m):
	if len(b[i]) >= k:
		print('Yes')
		for j in range(k):
			print(b[i][j],)
		break
else:
	print('No')
