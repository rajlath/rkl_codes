def next_2_power(n):
    if (n and not(n & (n-1))):
        return n
    count = 0
    while n != 0:
        n >>=1
        count += 1
    return 1 << count

noe = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr, reverse=True)
print(arr)
match = []
indx  = []
for i, v  in enumerate(arr):
    if v  in match:
        match.remove(v)
        indx.remove(match.index(v))
        continue
    else:
        nxt = next_2_power(v)
        match.append(nxt - v)
        indx.append(i)
    print(match, indx)



print(next_2_power(1023))