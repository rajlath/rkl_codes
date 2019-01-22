n, m = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a = [0] * n
for i in b:
    for j in range(i-1, n):
        print(j)
        if a[j] == 0: a[j] = str(i)
print(*a)        
