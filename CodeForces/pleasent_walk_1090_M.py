nb_house , nb_colors = [int(x) for x in input().split()]
house_colors         = [int(x) for x in input().split()]

curr = house_colors[0]
maxs = 1
curr_maxs = 1

for i in house_colors:
    if i != curr:
        curr_maxs += 1
    else:
        curr_maxs = 1
    maxs = max(maxs, curr_maxs)
    curr = i

print(maxs)
