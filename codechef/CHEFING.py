nb_Test = int(input())
for _ in range(nb_Test):
    nb_dish = int(input())
    ingrediants = {}
    for _ in range(nb_dish):
        curr = set(input())
        for i in curr:
            ingrediants[i] = ingrediants.get(i, 0) + 1
    common = 0
    for k, v in ingrediants.items():
        if v == nb_dish:
            common += 1

    print(common)
