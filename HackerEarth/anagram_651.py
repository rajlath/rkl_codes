from collections import Counter
nb_test = int(input())
for _ in range(nb_test):
    a = Counter(input())
    b = Counter(input())
    diff = 0
    for x in a:
        if x not in b:
            diff += a[x]
        else:
            diff += abs(a[x] - b[x])
    for x in b:
        if x not in a:
            diff += b[x]
    print(diff)


