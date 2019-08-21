for _ in range(int(input())):
    nb_cups, position, nb_ops = [int(x) for x in input().split()]
    for _ in range(nb_ops):
        left, rite  = [int(x) for x in input().split()]
        if position in range(left, rite + 1):
            if position - left < rite - position:
                position = rite - (position - left)
            else:
                position = left + (rite - position)
    print(position)
