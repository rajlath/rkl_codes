# Born this way

n, m, ta, tb, k = [int(x) for x in input().split()]
start_a = [int(x) for x in input().split()]
start_b = [int(x) for x in input().split()]
ans = 0
valid = -1
for i in range(m):
    if ans < n and start_a[ans] + ta <= start_b[i]:
        ans += 1
        k -= 1
        if k == -1:
            valid = start_b[i] + tb
            break
print(valid)
