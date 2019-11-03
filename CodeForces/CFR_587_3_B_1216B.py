nb = int(input())
ar = [int(x) for x in input().split()]
al = sorted([(v, i) for i, v in enumerate(ar)], reverse=True)
an = []
mu = 0
su = 0
for x, y in al:
    an.append(y + 1)
    su += (x * mu + 1)
    mu += 1
print(su)
print(*an)

