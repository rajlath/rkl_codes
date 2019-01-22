nb_bricks = int(input())
i = 1
while nb_bricks > 0:
    nb_bricks -= i
    if nb_bricks <= 0:
        print("Patlu")
        break
    nb_bricks -= i * 2
    if nb_bricks <= 0:
        print("Motu")
        break
    i += 1

