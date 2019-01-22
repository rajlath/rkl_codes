nb_friends = int(input())
limit = int(input())
for _ in range(nb_friends):
    print(("YES", "NO")[int(input()) < limit])

