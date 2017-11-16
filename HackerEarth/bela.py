'''
5
1 2 3 4 5
54
'''
maxs = 0
n = int(input())
a = [int(x) for x in input().split()]
sums = sum(a)
suma = 0
for i in range(n):
    suma += a[i]
    maxs = max(maxs, suma * (sums - suma))
print(maxs)    