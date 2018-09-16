noe = int(input())
arr = [int(x) for x in input().split()]
arr = set(arr)
for _ in range(int(input())):
    x = input().split()
    if len(x) == 1:
        arr.pop()
    if len(x) == 2:
        val = int(x[1])
        if x[0] == 'remove'  :
            if val in arr:
                arr.remove(val)
        else:
            arr.discard(val)
if len(arr) > 0: print(*arr)





