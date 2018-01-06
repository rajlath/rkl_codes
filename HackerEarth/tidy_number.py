for _ in range(int(input())):
    s = list(input())
    for i in range(len(s)-2, -1, -1):
        if int(s[i]) > int(s[i+1]):
            s[i] = str(int(s[i]) - 1)
            for j in range(i+1, len(s)):
                s[j] = "9"
    ans = ("".join(s))
    print(int(ans))

