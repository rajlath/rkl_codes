h, w = map(int, input().split())
a = []
s = 0

for i in range(1, h + 1):
    a.append([*input()])
    s += a[-1].count('*')

ans = 'NO'
if s <= h + w - 1:
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if a[i][j] == '*':
                u = l = r = d = 0
                k = j - 1
                while k >= 0 and a[i][k] == '*':
                    l += 1
                    k -= 1
                k = j + 1
                while k < w and a[i][k] == '*':
                    r += 1
                    k += 1
                k = i - 1
                while k >= 0 and a[k][j] == '*':
                    u += 1
                    k -= 1
                k = i + 1
                while k < h and a[k][j] == '*':
                    d += 1
                    k += 1
                if u and l and d and r and u + l + d + r + 1 == s:
                    ans = 'YES'
                    break
        if ans == 'YES':
            break

print(ans)