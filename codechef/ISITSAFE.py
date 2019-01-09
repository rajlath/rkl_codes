nb_test = int(input())
for _ in range(nb_test):
    valids = 0
    for _ in range(10):
        valids += sum([1 for x in input().split() if int(x) <= 30])
    print(['no', 'yes'][ valids >= 60])
