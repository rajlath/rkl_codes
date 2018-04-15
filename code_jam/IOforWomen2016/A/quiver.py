'''
3
5 2
1 3
10 2
3 6 7 8
7 3
1 5
'''
for _ in range(int(input())):
    hours, interval = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    M   = arr[0]
    cp  = arr[1:]
    hour = [0] * (hours+1)
    for i in cp:
        hour[i] = 1
    start = 0
    nexts = start + interval
    for i in range(1, hours+1):
        if hour[i] == 1:
            nexts = i + interval
            #print(nexts, "cp")
        else:
            if i == nexts:
                hour[i] = 1
                nexts = i + interval
                #print(nexts,"ncp")
        #print(i)
    print(sum(hour))









