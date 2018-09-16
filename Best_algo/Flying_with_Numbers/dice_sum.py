'''
Nos. of ways two dice will result in a particular sum
'''
from collections import Counter, defaultdict
def find_dice_probability(S, faces= 6):
    if S > 2 * faces or S < 2: return False
    cdict = Counter()
    ddict = defaultdict(list)
    for dice1 in range(1, faces+1):
        for dice2 in range(1, faces + 1):
            t = [dice1, dice2]
            cdict[sum(t)] += 1
            ddict[sum(t)].append(t)
    return [cdict[S], ddict[S]]
for i in range(2, 13):
    print(i,find_dice_probability(i, 12))



