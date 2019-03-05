'''
from collections import defaultdict
nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    string = input()
    counts = defaultdict(list)
    i = 1
    while i < (lens+1):
        currs = string[:i]
        currc = string.count(currs)
        counts[currc].append(currs)
        i += 1
    counts = sorted(counts.items(), key = lambda x: x[0], reverse=True)
    #print(counts)
    ans = counts[0][1]
    print(sorted(ans)[-1])
'''
from collections import defaultdict
nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    string = input()
    string = string + '-' * 10
    seq = []
    for x in range(1, lens):
        if string[x] == string[0]:
            seq.append(x)
    if not seq:
        print(string[:lens])
    else:
        flag = 1
        for x in range(1, seq[0]+1):
            if flag:
                for y in seq:
                    if string[y+x] is not string[x]:
                        temp = x
                        flag =0
                        break
            else:
                temp = x - 1
                break
        print(string[:temp])











