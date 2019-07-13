from collections import Counter


nb = int(input())
for _ in range(nb):
    lens = int(input())
    elem = Counter([int(x) for x in input().split()])
    key = 0
    ans = 0
    for k in elem:
        if k > key and ans <= ans:
            key = k
            ans = elem[k]
    print(key)
