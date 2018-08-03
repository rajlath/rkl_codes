'''
5 4
1 2 3 4 5
'''
nol, rounds = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
shifts = rounds % nol
curr = arr[:]
for i in range(shifts):
    for j in range(nol):
        x = (j + nol - 1)%nol
        arr[x] = curr[j]
    curr = arr[:]


print(*arr)