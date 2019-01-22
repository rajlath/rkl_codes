nb_pair = int(input())
drawn   = [int(x) for x in input().split()]
maxs = 1
table = set()
for i in drawn:
    table ^= {i}
    maxs = max(maxs, len(table))
print(maxs)

