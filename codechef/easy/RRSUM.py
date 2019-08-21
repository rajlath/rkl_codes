
n, q = [int(x) for x in input().split()]
mins = n + 2
maxs = 3 * n
avgs = (mins + maxs) // 2
for _ in range(q):
    current = int(input())
    if current < mins or current > maxs:
        print(0)
    elif current <= avgs:
        print(n + current - avgs)
    else:print(n + avgs - current)
