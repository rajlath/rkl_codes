a, b = [x for x in input().split()]
ans = a[0]
i = 1
j = 0
while i < len(a)  or j < len(b):
    if i >= len(a) or b[j] <  a[i]:
        ans += b[j]
        j += 1
        break
    else:
        ans += a[i]
        i += 1

print(ans)
