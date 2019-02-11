'''
nb_Test = int(input())
for _ in range(nb_Test):
    n, a, b, k = [int(x) for x in input().split()]
    problems = list(range(1, n+1))
    can_do = 0
    ans = "Lose"
    for i in problems:
        if i % (a * b) == 0:continue
        if i % a == 0: can_do += 1
        elif i % b == 0: can_do += 1
        if can_do >= k:
            ans =  "Win"
            break
    print(ans)


from collections import defaultdict
nb_Test = int(input())
for _ in range(nb_Test):
    n, a, b, k = [int(x) for x in input().split()]
    counts = [0] * (n+1)
    i = 1
    while i*a<= n or i*b <= n:
            if i*a <= n:counts[i*a] += 1
            if i*b <= n:counts[i*b] += 1
            i += 1
    sums = sum([x for x in counts if x == 1])
    print(["Lose", "Win"][sums >= k])


from collections import defaultdict
nb_Test = int(input())
for _ in range(nb_Test):
        n, a, b, k = [int(x) for x in input().split()]
        arr = list(range(1, n+1))
        ans = [x for x in arr if x%a==0 or x%b == 0 and x%(a*b) >= 2]
        print(ans)
'''
from math import ceil
nb_Test = int(input())
for _ in range(nb_Test):
        n, a, b, k = [int(x) for x in input().split()]
        ans = ceil(n / a) + ceil(n / b) - (2 * ceil( n / (a * b)))
        print(ans)
        if ans - k >= 0:
                print("Win")
        else:
                print("Lose")





