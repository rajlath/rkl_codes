nb_peoples = int(input())
ids = [int(x) for x in input().split()]
count = 0
for i in range(nb_peoples):
    curr = ids[i:]

    mins = curr.index(min(curr))

    if mins != 0:
        count += 1
        ids[i], ids[mins] = ids[mins], ids[i]
print(count)


