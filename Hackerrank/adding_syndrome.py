
for _ in range(int(input())):
    n = int(input())
    ans = sum([x for x in range(1, n+1) if x%2])
    print(ans)

