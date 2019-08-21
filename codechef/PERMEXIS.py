for _ in range(int(input())):
    n = int(input())
    l = sorted([int(x) for x in input().split()])
    can_be ="YES"
    for i in range(n - 1):
        if l[i+1] - l[i] > 1:
            can_be = "NO"
            break
    print(can_be)        
