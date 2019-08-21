from collections import defaultdict
for _ in range(int(input())):
    rooms, done = [int(x) for x in input().split()]
    visits = [int(x) for x in input().split()]
    bottles = []
    for i in range(rooms):
        indx,*volume = [int(x) for x in input().split()]
        bottles.append(volume)
    drunk = 0
    #print(bottles)
    for i in visits:
        curr = bottles[i]
        if len(curr)>0:
            indx = curr.index(max(curr))
            drunk += curr[indx]
            del bottles[i][indx]
    print(drunk)
