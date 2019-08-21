def find_parent(x):
    y = x
    while y != parent[y]:
        y = parent[y]
    while x != parent[x]:
        z = parent[x]
        parent[x] = y
        x = z
    return y

for _ in range(int(input())):
    N = int(input())
    S = [int(x) for x in input().split()]

    parent = [i for i in range(N)]
    chef   = [i for i in range(N)]
    for _ in range(int(input())):
        query = [int(x) for x in input().split()]
        if query[0] == 0:
            x = find_parent(query[1] - 1)
            y = find_parent(query[2] - 1)
            if x == y:
                print("Invalid query!")
            else:
                if S[chef[x]] > S[chef[y]]:
                    parent[y] = x
                    chef[y] = chef[x]
                elif S[chef[x]] < S[chef[y]]:
                    parent[x] = y
                    chef[x] = chef[y]
        else:
            print(chef[find_parent(query[1] - 1)] + 1)