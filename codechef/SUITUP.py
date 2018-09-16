for _ in range(int(input())):
    lens = int(input())
    src  = input().strip()
    max_diff = -1
    for i in src:
        max_diff = max(max_diff, src.rindex(i) - src.index(i))
    print(max_diff)





