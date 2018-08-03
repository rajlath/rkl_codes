noe = int(input())
arr = [int(x) for x in input().split()]
maxs= max(arr)
while m != (m & (-m)):
    m -= (m & (-m))
i, j = 1, 0
while j < 64:
    i <<= 1
    j += 1
    for k in range(n):
        arr