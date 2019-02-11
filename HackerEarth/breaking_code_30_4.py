nb_test = int(input())
for _ in range(nb_test):
    person, pair = [int(x) for x in input().split()]
    persons = [0] * person
    for _ in range(pair):
        a, b = [int(x) for x in input().split()]
        persons[a-1] = 1
        persons[b-1] = 1
    print("NO" if 0 in persons else "YES")