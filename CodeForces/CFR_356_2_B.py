nb_city, city = [int(x) for x in input().split()]
cities = [int(x) for x in input().split()]
city -= 1
l = city - 1
r = city + 1
ans = sum(cities)
while l >= 0 and r < nb_city:
    ans -= cities[l] ^ cities[r]
    l -= 1
    r += 1

print(ans)

