parents = {}
roots   = {}

def find_roots(parents, person):
    root = person
    while root in parents:
        root = parents[root]
    p = person
    while p != root:
        parent = parents[p]
        parents[p] = root
        p = parent
    return root
maxs = 1
for i in range(int(input())):
    l, r = [int(x) for x in input().split()]
    if l not in parents:
        parents[l] = -1
        roots[l]   =  1
    if r not in parents:
        parents[r] = -1
        roots[r]   =  1
    print(parents, roots)
    rootl = find_roots(parents, l)
    rootr = find_roots(parents, r)
    print(rootl, rootr)
    if rootl != rootr:
        parents[rootl] = root[r]
        roots[rootr] = roots[rootr] + roots[rootl]
        del roots[rootl]
        maxs = max(maxs, roots[rootr])
    else:
        result = maxs
    print(result)

