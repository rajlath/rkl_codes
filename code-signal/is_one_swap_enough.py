def isOneSwapEnough(inputString):
    invalid = [[], []]
    cnts = 0
    lens = len(inputString)
    for x, y in zip(inputString[:lens//2],inputString[lens//2:] ):
        if x != y:
            if cnts == 2:return False
        if x > y:
            x, y = y, x
        invalid[cnts] = [x, y]
        cnts += 1
    if cnts == 0: return True
    elif cnts == 1:
        if lens % 2 == 0:return False
        c = inputString[lens//2]
        return invalid[0][0] == c or invalid[0][1] == c
    else:
        return invalid[0][0] == invalid[1][0] and invalid[0][1] == invalid[1][1]

print(isOneSwapEnough("aabaa"))
