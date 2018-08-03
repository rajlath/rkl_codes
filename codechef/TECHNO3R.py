for _ in range(int(input())):
    noc = int(input())
    arr = [int(x) for x in input().split()]
    for _ in range(int(input())):
        l, r = [int(x)-1 for x in input().split()]
        print(sum(arr[l:r+1]))



