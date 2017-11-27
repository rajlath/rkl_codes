for _ in range(int(input())):
    ins = input()
    cnt = 0
    for i in ins:
        if i in "aeiouAEIOU":
            cnt+= 1
    print(cnt)  

