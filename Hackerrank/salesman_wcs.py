for _ in range(int(input())):
    loa = int(input())
    arr = [int(x) for x in input().split()]
    arr = sorted(arr)
    maxs = 0
    for i in range(1, loa):
        maxs += arr[i] - arr[i-1]
    print(maxs)
