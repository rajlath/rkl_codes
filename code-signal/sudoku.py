def sudoku(g):
    for i in range(9):
        if len(set(g[i]))!=9:
            return False
        c = [g[j][i] for j in range(9)]
        if len(set(c))!=9:
            return False
        s = [g[3*(3<=i<=5)+6*(6<=i<=8)+j][(3*i)%9+k] for j in range(3) for k in range(3)]
        print(s)
        if len(set(s))!=9:
            return False
    return True