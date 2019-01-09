noe, k, noq = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
for _ in range(noq):
    curr = int(input())
    print(arr[(curr + noe - k)%noe])