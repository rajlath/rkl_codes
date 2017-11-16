l, r, k = [int(x) for x in input().split()]
print(sum([1 for x in range(l, r+1) if x%k==0]))
