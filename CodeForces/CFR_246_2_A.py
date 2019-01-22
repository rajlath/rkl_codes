n, k = [int(x) for x in input().split()]
arrs = [int(x) for x in input().split()]
print( (sum(x <= 5 - k for x in arrs)) // 3 )