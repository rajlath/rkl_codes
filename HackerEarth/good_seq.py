from collections import Counter
nb_Test = int(input())
for _ in range(nb_Test):
    cnt = [x for x in list((Counter(input())).values())]
    ans = 1
    for i in cnt:
        ans *= i
        ans %=  int(10 ** 9 + 7)
    print(ans)