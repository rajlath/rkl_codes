
nb_tweet, ops = [int(x) for x in input().split()]
opens = 0
opened = []
for i in range(ops):
    curr = input()
    if curr == "CLOSEALL":
        opens = 0
        opened = []
    else:
        _,indx = [x for x in curr.split()]
        indx = int(indx)
        if indx in opened:
            opened.remove(indx)
            opens -= 1
        else:
            opens += 1
            opened.append(indx)
    print(opens)
