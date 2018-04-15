for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    qry = int(input())
    for _ in range(qry):
        l, r = [int(x)-1 for x in input().split()]
        print(sum(arr[l:r+1]))