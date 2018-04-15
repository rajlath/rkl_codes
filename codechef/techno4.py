'''
1

5

4 3 2 1 5

3

1 2

2 4

1 4
'''
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    sums=[0]*(noe+1)

    for i in range( noe):
        sums[i+1] = sums[i] + arr[i]

    for _ in range(int(input())):
        l, r = [int(x) for x in input().split()]
        print(sums[r] - sums[l-1])




