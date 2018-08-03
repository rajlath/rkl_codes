for _ in range(int(input())):
    noc, k = [int(x) for x in input().split()]
    s = input()
    cnt = 0
    display = []
    for i in range(noc-k + 1) :
        display.append(s[i:i+k])
    #print(display)

    for i in range(len(display)-2, -1, -1):
        #print(display[i+1], display[i])
        cnt += sum([1 for (a, b) in zip(display[i], display[i+1]) if a != b])
    print(cnt)




