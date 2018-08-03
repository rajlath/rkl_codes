'''
4 5
10101
01000
00111
10000
Output
YES

n, m = [int(x) for x in input().split()]
arr  = [[x for x in input()] for _ in range(n)]
k = [sum([int(x) for x in arr[i] if x=="1"]) for i in range(n)]
for i in range(n):
    x = 1
    for j in range(len(arr[i])):
        if k[j] - int(arr[i][j]) <= 0:
            x = 0
    if x == 1:break
print(["NO", "YES"][x == 1])
'''
n,m=map(int,input().split())
t=[list(input()) for _ in range(n)]
k=[0 for _ in range(m)]
for i in range(n):
    for j in range(m):
        if t[i][j]=='1':
            k[j]+=1

for i in range(n):
    x=1
    for j in range(len(t[i])):
        if (k[j]-int(t[i][j]))<=0:
            x=0
    if x==1:
        break
print(["NO", "YES"][x == 1])
