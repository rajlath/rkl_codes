n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in range(n-1, 0, -1):
    temp = 0
    for j in range(1, n+1):
        for k in range(n-1, 0, -1):
            if k >= i and i >= j and a[k] < a[i]:
                temp +=1
    ans += temp//i

print(ans)

