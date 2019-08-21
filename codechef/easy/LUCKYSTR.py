nb_fav, nb_pillow = [int(x) for x in input().split()]
favs = [input() for _ in range(nb_fav)]
counts = 0

for _ in range(nb_pillow):
    current = input()
    ans = "Bad"
    if len(current) > 46:
        ans = "Good"
    else:
        for i in favs:
            if i in current:
                ans = "Good"
                break
    print(ans)