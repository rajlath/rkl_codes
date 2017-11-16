import time 
N=15485864
a=[1]*N
for i in range(2, 3936):
    if a[i]:
        for j in range(i*i,N, i):a[j]=0
noe = int(input())
arr = [int(x) for x in input().split()]
queue = []
stack = []
for i in arr:
    if a[i] :
        queue.append(i)
    else:
        stack.append(i)    
        
print(" ".join(map(str, queue)))        
print(" ".join(map(str, stack)))
