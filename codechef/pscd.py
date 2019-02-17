nb_test = int(input())
for _ in range(nb_test):
    curr = [x for x in input()]
    for i in range(len(curr)):
        if int(curr[i]) < 5:
            curr[i] = str(9 - curr[i])
    print("".join(curr))

