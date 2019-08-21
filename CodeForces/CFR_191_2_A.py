
from  itertools import groupby
n = int(input())
a = [int(x) for x in input().split()]
ones = a.count(1)
answer = [sum(a)-2*sum(a[i:j])+j-i for i in range(n) for j in range(i+1,n+1)]
print(max(answer))


'''
n = int(input())
a = [int(i) for i in input().split()][:n]
x = 
print(x)
print(max())
'''
