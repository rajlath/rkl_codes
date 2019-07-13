def VowelSquare(strArr):
    grid = [[x for x in a] for a in strArr]
    rows = len(grid)
    cols = len(grid[0])
    i, j = 0, 0
    ans = "not found"
    while i < rows - 1:
        j = 0
        while j < cols - 1:
            current = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
            valid = True
            for x in current:
                if x not in "aeiou":
                    valid = False
                    break
            if valid:
                ans = (str(i) +"-" +str(j))
                break
            j += 1
        i += 1
        if ans != "not found":break
    return ans


print(VowelSquare(["gg", "ff"]))
