nb_test = int(input())
for _ in range(nb_test):
    nb_city = int(input())
    cities = [x[0] for x in input() for _ in range(nb_city)]
    print(["NO", "YES"][nb_city == len(set(cities))])