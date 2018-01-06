
N, Q = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

a.append(0)
pos = [0] * (N+5)
val = [0] * (N+5)
sums= [0] * (N+5)

def get(L, R):
    le = L
    ri = R
    mi = 0
    global val

    while (le+1) < ri:
        mi = (le + ri) >> 1
        #print(le, mi, ri)
        if val[mi] <= L:le = mi
        else:           ri = mi
    if val[ri] <= L:return ri
    return le

def calc(n):
    return n * (n + 1) // 2


cur = 0
for i in range(N):
    cur = max(cur, pos[a[i]])
    val[i] = cur
    pos[a[i]] = i
    sums[i] = i - cur + 1
    sums[i] += sums[i - 1]
print(sums)



for i in range(Q):
    le, ri = [int(x) for x in input().split()]
    mi = get(le, ri)

    ans = sums[ri] - sums[mi] + calc(mi-le + 1)
    print(ans)





