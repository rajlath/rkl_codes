for _ in range(int(input())):
    choc,frnd = [int(x) for x in input().split()]
    ans = -1
    for i in range(1, choc):
        curr = ((choc * 2) / frnd - 2 * i) / (frnd - 1)
        if curr == round(curr) and curr != 0:
            ans = curr
            break
        if curr < 0:
            ans = -1
            break
    if ans == -1:
        print("N")
    else:
        print("Y", i)