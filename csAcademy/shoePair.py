L, R = [],[]
for _ in range(int(input())):
    a, b = [x for x in input().split()]
    if b == "L": L.append(a)
    else: R.append(a)
cnt = 0

if len(L) > len(R):
    L, R = R, L
for i in L:
    if i in R:
        del R[R.index(i)]
        cnt += 1
print(cnt)