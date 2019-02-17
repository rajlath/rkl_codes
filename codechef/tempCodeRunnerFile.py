nb_test = int(input())
for _ in range(nb_test):
    curr = [int(x) for x in input()]
    for i in range(len(curr)):
        if curr[i] < 5:
            curr[i] = 9 - curr[i]
    print("".join(map(str, curr)))

