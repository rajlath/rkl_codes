for _ in range(int(input())):
    front = input()
    backs = input()

    Bs = 0
    Os = 0
    oo = 0

    for i in range(len(front)):
        if front[i] == "b"  or backs[i] == "b":
            Bs += 1
        if front[i] == "o"  or backs[i] == "o":
            Os += 1
        if front[i] != "b" and backs[i] != "b" and front[i] != "o" and backs[i] != "o":
            oo += 1
    if Bs == 2 and Os == 1 and oo == 0:
        print("yes")
    else:
       print("no")





