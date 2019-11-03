nb_flowers = int(input())
beauties = [int(x) for x in input().split()]
mins = min(beauties)
maxs = max(beauties)
max_beauty = maxs - mins
if mins == maxs:
    nb_ways = (nb_flowers * ( nb_flowers - 1))//2
else:
    nb_ways = beauties.count(mins) * beauties.count(maxs)
print(max_beauty, nb_ways)