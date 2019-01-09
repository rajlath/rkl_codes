
def calc(f, t, m):
    count = 0
    for i in range(1, f+1):
        for j in range(1, t+1):
            if (i*i + j*j)%m == 0:
                count += 1
    return count

n, m = [int(x) for x in input().split()]
c, r = divmod(n, m)
m2m  = calc(m, m, m)
r2m  = calc(r, m, m)
r2r  = calc(r, r, m)
ans  = m2m * c * c  + 2 * r2m * c + r2r
print(ans)


