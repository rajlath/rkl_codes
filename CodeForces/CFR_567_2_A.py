sasha, masha, cost = [int(x) for x in input().split()]
coconuts = (sasha // cost) + (masha // cost)
sasha_left, masha_left = sasha % cost, masha % cost
if sasha_left == 0 and masha_left == 0:
    print(coconuts, 0)
else:
    if sasha_left + masha_left >= cost:
        shasa_need = cost - sasha_left
        masha_need = cost - masha_left
        print(coconuts + 1, min(shasa_need, masha_need))
    else:
        print(coconuts, 0)
