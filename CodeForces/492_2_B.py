n = int(input())
a = [int(x) for x in input().split()]
ind = min(a)
for i in range(n):
    if a[ind%n] > ind:
        ind += 1
print(ind%n + 1)
