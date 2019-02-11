nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    maxs = -1
    curr = 0
    while curr <= lens:
        if (lens - curr) % 5 == 0:
            maxs = max(maxs, int("5" * (curr) + "3" * (lens - curr)))
        curr += 3
    print(maxs)





