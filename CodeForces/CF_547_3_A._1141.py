a, b = [int(x) for x in input().split()]
i = 0
j = 0
ans = -1
for i in range(30):
    for j in range(30):
        if a * (2 ** i) *  (3 ** j) == b:
            ans = i + j
            break
print(ans)
