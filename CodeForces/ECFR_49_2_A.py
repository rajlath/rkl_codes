for _ in range(int(input())):
    lens = int(input())
    ins  = input()
    ans  = "YES"
    for x, y in zip(ins, ins[::-1]):

        if ord(x) - ord(y) not in [2, 0, - 2]:
            ans = "NO"
            break
    print(ans)
