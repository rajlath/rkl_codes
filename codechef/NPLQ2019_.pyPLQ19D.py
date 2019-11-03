for _ in range(int(input())):
    curr = input()
    rets =''
    for i in curr:
        if not i in rets:
            rets += i
    print(rets)