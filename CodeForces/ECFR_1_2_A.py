nb_test = int(input())
for _ in range(nb_test):
    ins = int(input())
    sums = ins * (ins + 1) // 2
    twos = 1
    while twos <= ins:
        twos *= 2
        sums -= twos
    print(sums)