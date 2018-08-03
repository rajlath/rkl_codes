n = input()
a = [int(x) for x in input().split()]
maxs = max(a)
print(sum([maxs - x for x in a]))