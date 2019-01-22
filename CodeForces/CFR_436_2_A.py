n = int(input())
a = [int(input()) for _ in range(n)]
a1 = list(set(a))
if len(a1) == 2 and a.count(a1[0]) == a.count(a1[1]):
    print("YES")
    print(*a1)
else:
    print("NO")




