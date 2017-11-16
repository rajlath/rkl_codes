'''
Sample Input 1

3 3
1 3 4
2 2 3 
1 2 4
Sample Output 1

60
'''
maxn = 105

flag = [[0]*maxn]*maxn


ud=0
maxs=-1e9
m,n = [int(x) for x in input().split()]
lst  = []

for i in range(n):
    tmp = [int(x) for x in input().split()]
    ud += sum([1 for x in tmp if x >0])
    maxs = max(maxs, max(tmp))
    lst.append(tmp)
    
sums = (ud * 2)
for i in range(maxs):
    for j in range(m):
        for k in range(n):
            if lst[j][k] > 0:
                flag[j][k] = 1
    for j in range(m):
        for k in range(n):
            if flag[j][k]:
                if flag[j-1][k] == 0: sums +=1
                if flag[j][k-1] == 0: sums +=1
                if flag[j+1][k] == 0: sums +=1
                if flag[j][k+1] == 0: sums +=1
    for j in range(m):
        for k in range(n):
            lst[j][k] -= 1
                

print(sums)
    






