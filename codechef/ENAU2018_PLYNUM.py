def bfs(x, y):
    maxs = 2005
    arr = [-1] * maxs
    q =[x]
    arr[x] = 0
    while q:
        x = q.pop(0)
        if x == y:
            return arr[x]
        if x -1 >= 0 and arr[x-1] == -1:
            arr[x-1] = 1 + arr[x]
            q.append(x-1)
        if x + 3 < maxs and arr[x+3] == -1:
            arr[x+3] = 1 + arr[x]
            q.append(x+3)
        if x * 2 < maxs  and arr[2 * x] == -1:
            arr[2 * x] = 1 + arr[x]
            q.append(2 * x)
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a == b:
        print("0")
    else:
        print(bfs(a, b))



