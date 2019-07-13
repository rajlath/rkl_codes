nb = int(input())
ar = [-x - 1 if x >= 0 else x for x in map(int,input().split())]
#print(ar)
min_index = ar.index(min(ar))
if nb % 2: ar[min_index] = -ar[min_index] - 1
print(*ar)
