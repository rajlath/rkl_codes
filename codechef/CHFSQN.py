n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
sums = 0
for i in range(n//2):
    sums += (2 * a[n-i-1] - 2 * a[i])
print(sums)
