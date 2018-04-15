for _ in range(int(input())):
    ans = "Happy Alex"
    a, b = [int(x) for x in input().split()]
    if a == b:
        ans = "Poor Alex"
        break
print(ans)
