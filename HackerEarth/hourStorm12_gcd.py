n, k = [int(x) for x in input().split()]
arrs = [int(x) for x in input().split()]
print(max([(i ^ k) * i for i in arrs] ))
