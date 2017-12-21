'''
SAMPLE INPUT
3 4
1 2 3
0 1 L
1 3 L
2 1 R
1 5 L
SAMPLE OUTPUT
0
2
1
-1
'''
city_cnt, qry_cnt = [int(x) for x in input().split()]
cities = [int(x) for x in input().split()]
city_both = []
for i, v in enumerate(cities):
    city_both.append((cities[(i-1+city_cnt)%city_cnt], cities[(i+1)%city_cnt]))
print(city_both)

for i in range(qry_cnt):
    start,types,direction = [x for x in input().split()]
    cnt  = -1
    way  = [0, 1][direction=="R"]
    start, types = int(start), int(types)
    for j, v in enumerate(city_both, start=start-1):
        print(j, v)
        if v[way] == types:
            cnt = j - start
            break
    print(cnt)





