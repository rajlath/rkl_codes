'''
nb_Test = int(input())
for _ in range(nb_Test):
    curr = input()
    counts = sorted([curr.count(i) for i in set(curr)], reverse=True)
    lens = len(curr)
    uniq_ch = len(set(curr))
    sames = 0
    for i in range(uniq_ch, -1, -1):
        if lens % i == 0:
            sames = i
            break
    ops = 0
    for i in range(sames):
        ops += abs(counts[i] - sames)
    print(ops)
'''
from string import ascii_uppercase as au
alpha_val = dict(zip(au, list(range(1, 27))))
nb_test = int(input())
for _ in range(nb_test):
    curr = input()
    lens = len(curr)
    alpha= [0] * 27
    for i in curr:
        alpha[alpha_val[i]] += 1
    alpha = sorted(alpha, reverse=True)
    mins = lens + 1
    for i in range(1, 27):
        if lens % i == 0:
            this = lens // i
            will = 0
            for f in range(i):
                if this > alpha[f]:
                    will += (this - alpha[f])
            if will <= mins:
                mins = will
    print([mins, 0][mins == lens + 1])







