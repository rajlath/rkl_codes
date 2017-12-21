'''
3 4
1 2 3
0 1 L
1 3 L
2 1 R
1 5 L
'''
city_cnt, query_cnt = [int(x) for x in input().split()]
cities = [int(x) for x in input().split()]
for i in range(query_cnt):
    begins, target, ways = [x for x in input().split()]
    nexts = int(begins)
    target= int(target)
    moves = -1
    found = False
    for i in range(city_cnt):
        print(cities[nexts], target)
        moves += 1
        if cities[nexts] == target:
            found = True
            break
        else:
            if ways == "R":
                nexts = (nexts + 1)%city_cnt
            else:
                nexts = (nexts - 1 + city_cnt)%city_cnt
    if found:print(moves)
    else:print(-1)








