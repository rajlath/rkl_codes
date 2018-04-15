a, b = [int(x) for x in input().split()]
fa = [int(x) for x in input().split()]
fb = [int(x) for x in input().split()]
fas = [fa[0]]
fbs = [fb[0]]


for i in range(1, a):
    fas.append(fas[-1]+fa[i])

for i in range(1, b):
    fbs.append(fbs[-1]+fb[i])
print(fas, fbs)

cnt = 0
for i in fas:
    while fbs[j] != i and j < b:
        j += 1

print(cnt)


