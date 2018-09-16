noe = int(input())
arr = [int(x) for x in input().split()]
l, r = 0, noe-1
lsum, rsum, maxsum = 0, 0, 0
while l <= r:
    if lsum >= rsum:
       rsum += arr[r]
       r-=1
    else:
        lsum += arr[l]
        l += 1
    if lsum == rsum:
        maxsum = lsum
print(maxsum)