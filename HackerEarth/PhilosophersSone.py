hb = list()
mb = list()
totals = 0
hnoc = int(input())
hb=[int(x) for x in input().split()]
noq, needed = [int(x) for x in input().split()]
for i in range(noq):
    curr = input()
    if curr  == "Harry":
        if len(hb)> 0:
            mb.append(hb[0])
            hb = hb[1:]
            inmb = sum(mb)
            #print(inmb)
            if inmb == needed:
                print(len(mb))
                break
        else:
            print(-1)
            break
    if curr ==  "Remove":
        #print(mb)
        if len(mb)==0:
            print(-1)
            break
        removed = mb.pop()
        if sum(mb)==needed:
            print(len(mb))
            break
            
            
