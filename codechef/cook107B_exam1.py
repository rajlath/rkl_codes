nb_Test = int(input())
for _ in range(nb_Test):
    lens = int(input())
    sols = input()
    done = input()
    score = 0
    i = 0
    while i < lens:
        if sols[i] == done[i]:
            score += 1
            i += 1
        elif done[i] == "N":
            i += 1
        else:
            i += 2
        if i >= lens:break
    print(score)
