for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    arr  = [int(x) for x in input().split()]
    xors = 0
    for i in range(n):
        xors ^= arr[i]
    print(xors ^ k)