from collections import defaultdict
nb_test = int(input())
for _ in range(nb_test):
    person = int(input())
    friends = defaultdict(list)
    pairs = int(input())
    for i in range(pairs):
        a, b = [int(x) for x in input().split()]
        friends[a].append(b)
        friends[b].append(a)
    print(friends)

