lens = int(input())
arrs = [int(x) for x in input().split()]
arrss= sorted(arrs)
for i in range(lens):
    for j in range(lens-2):
        if arrs[j] > arrs[j+2]:
            arrs[j], arrs[j+2] = arrs[j+2], arrs[j]

ans = "OK"
for i, v in enumerate(arrs):
    if v != arrss[i]:
        ans = str(i)
        break
print(ans)
