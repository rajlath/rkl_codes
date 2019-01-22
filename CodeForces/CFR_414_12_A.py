a, b, c = [int(x) for x in input().split()]
d = 0
n = input()
aa = [x for x in input().split()]
ans = sum([1 for x in aa if b < int(x) < c])
print(ans)