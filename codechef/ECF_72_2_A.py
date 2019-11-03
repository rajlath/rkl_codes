for _ in range(int(input())):
    s, i, e = [int(x) for x in input().split()]
    to_add  = max(0, (e + i - s + 2)//2)
    print(max(e - to_add + 1, 0))