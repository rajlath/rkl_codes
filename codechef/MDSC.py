mod = int(10e18)
ans = 0
def dp(i, j, rc, values, status):
    global ans
    cache = [[-1 for x in range(rc)] for y in range(rc)]
    print(cache, i, j)
    if i > rc or i > rc:return mod
    if i == rc and j == rc: return values[i][j]
    ans = cache[i][j]
    if ans != -1:return ans
    ans = mod
    ans = min(ans, values[i][j] + dp(i+1, j, rc, values, status))
    ans = min(ans, values[i][j] + dp(i, j+1, rc, values, status))
    print(ans)



nb_test = int(input())
for _ in range(nb_test):
    rc = int(input())
    values = [[x for x in input().split()] for _ in range(rc)]
    status1 = [[x for x in input().split()] for _ in range(rc)]
    status = [[mod if x == '0' else 1 for x in status1[i] ] for i in range(rc)]
    dp(0, 0, rc, values, status)
    if ans > int(10e12):
        print("No")
    else:
        print("yes", ans)
