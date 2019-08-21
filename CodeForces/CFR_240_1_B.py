n, k = map(int, input().split())
d = 1000000007

n += 1
r = [{} for i in range(n)]  # multiples
for i in range(2, n):
    if r[i] == {}:
        for j in range(i, n, i): r[j][i] = 1
        q = i * i
        while q < n:
            for j in range(q, n, q): r[j][i] += 1
            q *= i

c = [1, k] + [0] * 9  # binomial
k -= 1
for i in range(2, 11): c[i] = (c[i - 1] * (k + i)) // i

s = -1
for q in r:
    p = 1
    for i in q.values(): p = p * c[i]
    s += p

print(s % d)