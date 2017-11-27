for _ in range(int(input())):
    s = input()
    vowels = "aeiou"
    ans = ""
    for i in s:
        if i in vowels:continue
        else:
            ans += "."+i.lower
    print(ans)
