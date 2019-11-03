for _ in range(int(input())):
    a, b, n = [int(x) for x in input().split()]
    arr = [a, b, a ^ b]
    print(arr[n % 3])

