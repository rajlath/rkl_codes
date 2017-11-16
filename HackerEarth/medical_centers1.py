n,k,m = [int(x) for x in input().split()]
'''
n : no of possible locations
k : no of medical centres
m : no of inital clients
'''
mn = -11111
# op : k space seperated integers
 
p = [[0]*n]
# m clients are of 1 based index
for x in range(m):
    p.append([int(x) for x in input().split()])
 
cost = [int(x) for x in input().split()]
 
##print(n,k,m)
##for x in p:
##    print(x)
##print(cost)
##
 
for x in range(n):
	for y in range(m+1):
		p[0][x] += p[y][x]
 
print(p) 
profit = [x-y for x,y in zip(p[0],cost)]
 
ans = []
for x in range(k):
	i = profit.index(max(profit))
	ans.append(i+1)
	profit[i] = mn
 
print(*ans)
