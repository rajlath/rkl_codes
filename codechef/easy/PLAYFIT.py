for _ in range(int(input())):
    lens = int(input())
    goal = [int(x) for x in input().split()]
    maxs = int(10e18)
    diff = -1
    for i in range(lens):
        diff = max(diff, goal[i] - maxs)
        maxs = min(maxs, goal[i])
    print(["UNFIT", diff][diff > 0])

