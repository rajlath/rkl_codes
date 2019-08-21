for _ in range(int(input())):
    lens, k = [int(x) for x in input().split()]
    esum = sum([1 for x in input().split() if int(x) % 2 == 0])
    if (k == 0) and (esum == lens):
        print("NO")
    elif esum >= k:
        print("YES")
    else:
        print("NO")
