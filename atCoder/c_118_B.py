nb_people, nb_foods = [int(x) for x in input().split()]
like_count = {}
for _ in range(nb_people):
    _, *liked = [int(x) for x in input().split()]
    for i in liked:
        like_count[i] = like_count.get(i, 0) + 1
cnt = 0
for x in like_count.values():
    if x == nb_people:
       cnt += 1
print(cnt)


