from collections import Counter
nb_test = int(input())
for _ in range(nb_test):
    ins = Counter(input()).most_common()
    maxs = -1
    wins = ''
    for k, v in ins:
        if v > maxs:
            wins = k
        elif maxs == v:
            if v < wins:
                wins = v
    print(wins)



