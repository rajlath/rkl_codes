given = [x for x in input()]
last = -1
for i in range(len(given) - 1):
    if given[i] in "02468":
        last = i
        if given[i] < given[-1]:
            break
if last == -1:
    print(-1)
else:
    given[last], given[-1] = given[-1], given[last]
    print(''.join(given))
