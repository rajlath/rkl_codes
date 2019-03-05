from collections import defaultdict
ans = "YeS"
def solve():
    nb_peoples = int(input())
    members = []
    for i in range(1, nb_peoples + 1):
        members.append(i)

    grouped = [0 for i in range(nb_peoples + 1)]
    group   = 1
    friends = int(input())
    friend_list = defaultdict(list)
    for _ in range(friends):
        u, v = [int(x) for x in input().split()]
        friend_list[u].append(v)
        friend_list[v].append(u)

    def dfs(i, gr)    :
        global ans
        if grouped[i]:
            if gr != group:
                ans = "No"
                return
        elif ans == "YeS":
            grouped[i] = 1
            for j in friend_list[i]:
                dfs(j, group ^ 1)

    for x in members:
        if ans == "No":break
        if not grouped[x]:
            dfs(x, 0)

    print(ans)

nb_test = int(input())
for _ in range(nb_test):
    solve()

