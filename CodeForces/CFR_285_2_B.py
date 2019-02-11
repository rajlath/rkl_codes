nb_user = int(input())
changes = {}
for _ in range(nb_user):
    old, new = [x for x in input().split()]
    if old in changes:
        changes[new] = changes[old]
        del changes[old]
    else:
        changes[new] = old
print(len(changes))
for k in changes:
    print(changes[k], k)
