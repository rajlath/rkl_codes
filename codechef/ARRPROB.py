
for _ in range(int(input())):
    n = int(input())
    arr= [int(x) for x in input().split()]
    sums= sum(arr)
    ans = [sums - x for x in arr]
    print(*ans)
