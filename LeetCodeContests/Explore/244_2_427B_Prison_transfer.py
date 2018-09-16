n, t, c = [int(x) for x in input().split()]
ex_id = [-1] + [i for i, v in enumerate(input().split()) if int(v) > t] + [n]
ans = 0
for i in range(1, len(ex_id)):
    diff = ex_id[i] - ex_id[i-1] - 1
    ans += max(diff- c + 1, 0)
print(ans)