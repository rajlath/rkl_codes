for _ in range(int(input())):
    levels = int(input())
    leaves = [int(x) for x in input().split()]
    branch , stem = 0, 0
    flag = 0
    for i in range(levels - 1, 0, -1):
        branch = leaves[i] + stem
        if branch % 2 == 1:
            flag = 1
            break
        else:
            stem = branch // 2
    if stem != 1:flag = 1
    if levels == 1 and leaves[0]  == 1:flag = 0
    print(["No", "Yes"][flag == 0])
