'''
5
1 2 6 4 6
'''
n,c,a,k=int(input()),0,[int(x) for x in input().split()],True
for i in range(1, n):
    if abs(a[i]-a[i-1])>2 and abs(a[i+1]-a[i-1])>2:c+=1
    if c>1:
        k=False
        break
print(k)