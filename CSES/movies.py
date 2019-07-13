nb_movies = int(input())
movies = []
for _ in range(nb_movies):
    x, y = [int(x) for x in input().split()]
    movies.append((y, x))
movies = sorted(movies)
#print(movies)
s = 0
c = 0
for a in movies:
    y, x = a
    if x >= s:
        s = y
        c += 1
print(c)
