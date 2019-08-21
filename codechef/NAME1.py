for _ in range(int(input())):
    parent = sorted("".join([x for x in input().split()]))
    childs = sorted("".join([input() for _ in range(int(input()))]))
    pi = 0
    ci = 0
    while pi < len(parent) and ci < len(childs):
        if parent[pi] == childs[ci]:
            pi += 1
            ci += 1
        else:
            pi += 1
    print(["No", "Yes"][ci == len(childs)])        
        
                     