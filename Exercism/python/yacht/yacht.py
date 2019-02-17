# Score categories
# Change the values as you see fit

from collections import Counter

def four_of_a_kind(dice):
    cdice = Counter(dice)
    for k, v in cdice.items():
        if v >= 4:
            return k * 4
    return 0

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES   = lambda dice:sum([1 for x in dice if x == 1])
TWOS   = lambda dice:sum([2 for x in dice if x == 2])
THREES = lambda dice:sum([3 for x in dice if x == 3])
FOURS  = lambda dice:sum([4 for x in dice if x == 4])
FIVES  = lambda dice:sum([5 for x in dice if x == 5])
SIXES  = lambda dice:sum([6 for x in dice if x == 6])
FULL_HOUSE = lambda dice:sum(dice) if len(set(dice)) == 2 and dice.count(list(set(dice))[0]) in [2, 3] else 0
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT =  lambda dice: 30 if set(dice) == set(range(1, 6)) else 0
BIG_STRAIGHT = lambda dice: 30 if set(dice) == set(range(2, 7)) else 0
CHOICE = lambda dice:sum(x for x in dice)






def score(dice, categeory):
    return categeory(dice)

