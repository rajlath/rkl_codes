for _ in range(int(input())):
    had = []
    events, has = [int(x) for x in input().split()]
    for i in range(events):
        ins = input().split()        
        if ins[0] == "P":
            had.append(has)
            has = int(ins[1])
        if ins[0] == "B" :
            tmp = has
            has = had.pop()
            had.append(tmp)
           
    print(has)           
