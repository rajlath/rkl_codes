import sys

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return (None, None)


inputs , outs = get_input_output()
indx = 0
test = 1

if inputs != None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        r, c , nb_monsters = [int(x) for x in inputs[indx].split()]
        indx += 1
        grids = [[0 for _ in range(c+1)] for _ in range(r+1)]
        monst = [[0 for _ in range(c+1)] for _ in range(r+1)]
        for _ in range(nb_monsters):
            x, y = [int(x) for x in inputs[indx].split()]
            indx += 1
            monst[x][y] = 1
        ans = 0
        for i in range(r)    :
            for j in range(c):
                if monst[i][j] == 0:
                    grids[i][j] = min(min(grids[i+1][j], grids[i][j+1]),grids[i+1][j+1])+1
                    ans += grids[i][j]
        ans = "Case #{}: {}".format(test, ans)
        print(ans, file=outs)
        test += 1
else:
    print("Invalid Input File.")


