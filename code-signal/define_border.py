def addBorder(picture):
    lens = len(picture[0])
    ans  = [['*' for x in range(lens + 2)] for y in range(len(picture)+2)]
    i = 1
    for x in picture:
        for m,v in enumerate(x):
            ans[i][m+1] = v
        i += 1
    return ["".join(x) for x in ans]





print(addBorder(["abc","ded"]))