from statistics import mean
nos = int(input())
score = [int(x) for x in input().split()]
means = round(mean(score))
added = 0
if means >= 4.5:print(0)
else:
    tmp = score[:]
    found = False
    for i, v in enumerate(score):
        if v != 5:
            for x in range(v+1, 6):
                added += 1
                tmp[i] = x
                print(tmp)
                means = mean(tmp)
                print(means)
                if means >= 4.5:
                    print(added)
                    found = True
                    break
        if found: break




