for _ in range(int(input())):
    a, b = [x for x in input().split()]
    a1 = "*"
    b1 = "$"
    s = list(input())
    for i in range(len(s)):
        if s[i] == a: s[i] = a1
        if s[i] == b: s[i] = b1
    for i in range(len(s)):
        if   s[i]  == a1 : s[i] = b
        elif s[i]  == b1 : s[i] = a

    print("".join(s))
