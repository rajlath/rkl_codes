nb = int(input())
for _ in range(nb):
    n = int(input())
    arr = [int(x) for x in input().split()]
    while n > 2:
        curr = sorted(arr[:3])
        arr.pop(arr.index(curr[1]))
        n -= 1
    print(*arr)