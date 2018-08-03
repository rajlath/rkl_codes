from collections import Counter
n, m = [int(x) for x in input().split()]
arrc  = Counter([int(x) for x in input().split()])
arrs  = sorted(arrc)[::-1]
cnt = 0
while arrs:
    curr = arrs.pop()
    if not arrs or arrs[-1] > curr + m:
        cnt += arrc[curr]
print(cnt)