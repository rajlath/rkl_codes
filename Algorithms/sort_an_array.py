A = [-5, 3, 2, - 1, 4, -8]
"""
ans = []
cnt = 0
for i in A:
    if i != 0:
        cnt += 1
        ans.append(i)
ans += [0]*cnt
print(ans)
"""
ans = []
for i in A:
    if i < 0:
        ans = [i] + ans
    else:
        ans += [i]
print(ans)


