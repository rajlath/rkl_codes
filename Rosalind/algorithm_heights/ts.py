def dfs(f, t, v, p, i):
    v[i] = True
    p.append(i)
    for adj in t[i]:
        if not v[adj]:
            f[adj].remove(i)
            if len(f[adj]) == 0:
                dfs(f, t, v, p, adj)

def topological_sort(f, t):
    visited = [False] * len(f)
    paths   = []
    for i in range(len(visited)):
        if not visited[i] and len(f[i]) == 0:
            dfs(f, t, visited, paths, i)
    return paths

def main():
    ifile = open("rosalind_ts.txt", "r")
    wfile = open("rosalind_ts_ans.txt", "w")

    n, e = [int(x) for x in ifile.readline().split()]
    froms = [set() for _ in range(n)]
    tos   = [[]    for _ in range(n)]
    for _ in range(e):
        u, v = [int(x) for x in ifile.readline().split()]
        froms[v-1].add(u - 1)
        tos[u - 1].append(v - 1)
    rets = [x+1 for x in topological_sort(froms, tos)]
    print(*rets, file = wfile)

if __name__ == "__main__":
    main()
