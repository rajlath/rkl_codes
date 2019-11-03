
lens = int(input())
vals = [int(x) for x in input().split()]

ans = 0
maxs = 0

for i in range(lens - 1):
    if vals[i] >= vals[i + 1]:
        ans += 1
    else:
        maxs = max(maxs, ans)
        ans = 0

print(max(maxs, ans))

