for _ in range(int(input())):
    ins = input()
    ans = 0
    open = 0
    close= ins.count(")")
    for curr in ins:
        if curr == "(":
            open += 1
            ans = max(ans, min(open, close) * 2)
        else:
            close -= 1
    print(ans)        
