for _ in range(int(input())):
    nod = int(input())
    uat = 0
    for _ in range(nod):
        a, b = [int(x) for x in input().split()]
        uat = max(0, b - a + uat)
    print(1 if uat > 0 else 0)