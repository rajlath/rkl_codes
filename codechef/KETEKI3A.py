for _ in range(int(input())):
    energy = int(input())
    apples = 0
    alls   = 0
    if energy == 1:
        apples = 1
        alls   = 1
    elif energy % 2 == 0:
        apples = 0
        alls   = energy // 2
    else:
        energy -= 3
        alls += 1
        alls += energy // 2
        apples = 0
    print(apples, alls)
