noe = int(input())
arr = [int(x) for x in input().split()]
sarr= sorted(arr)

need = -1
for i in range(1, noe):
    if sarr[i] == sarr[i-1]:
        need = sarr[i]
        break
need = sarr[i]

indices = sorted([i for i, x in enumerate(arr) if x ==need])

mins = 10e9
for x in range(1, len(indices)):
    mins = min(mins, indices[x] - indices[x-1])
print(mins)

