nb_test = int(input())
for _ in range(nb_test):
    nb_city = int(input())
    cities = []
    for _ in range(nb_city):
        cities.append(input()[0])
    print(["NO", "YES"][nb_city == len(set(cities))])