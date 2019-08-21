t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mini = min(a)
    if mini < 2:
        print(-1)
    else:
        print(sum(a) - mini + 2)
