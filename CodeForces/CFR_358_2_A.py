n, m = [int(x) for x in input().split()]
print(sum([ (m + i%5)//5  for i in range(1, n + 1)]))
