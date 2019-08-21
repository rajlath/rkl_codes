n = int(input())
arrs = [int(x) for x in input().split()]
i = 0
while i < n -1 and arrs[i] < arrs[i+1]:
    i += 1
while i < n - 1 and arrs[i] > arrs[i+1]:
    i += 1
print(["NO", "YES"][i == n - 1])
