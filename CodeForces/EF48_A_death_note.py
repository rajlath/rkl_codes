days, max_name = [int(x) for x in input().split()]
names = [int(x) for x in input().split()]
ends = 0
for i in range(days):
    ends += names[i]
    p, r = divmod(ends, max_name)
    print(p, end=" ")
    ends = ends - (p*max_name)



