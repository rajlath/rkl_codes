dominant = [11, 4, 3, 20, 10, 14, 0, 0 ]
non_domi = [11, 4, 3,  2, 10,  0, 0, 0 ]
indexes  = "AKQJT987"
nb_hands, doms = [x for x in input().split()]
nb_hands = int(nb_hands)
sums = 0
for i in range(nb_hands * 4):
    ins = input()
    k, suit = ins[0], ins[1]
    if k in indexes:
        indx = indexes.find(k)
    else:
        indx = -1
    if suit == doms:
        sums += dominant[indx]
    else:
        sums += non_domi[indx]
print(sums)



