'''
2
4 4
2 1 6 7
4 2
2 1 5 4

Output:

1
0
'''
for _ in range(int(input())):
    noe, k = [int(x) for x in input().split()]
    arr    = [int(x) for x in input().split()]
    sums   = sum(arr)
    ans    = sum([1 for x in arr if sums - x < x + k])
    print(ans)