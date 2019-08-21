def chessKnightMoves(cell):
    X = (2, 1, -1, -2,-2, -1, 1, 2)
    Y = (1, 2, 2, 1,-1, -2, -2, -1)
    cando = 0
    kx, ky = "abcdefgh".index(cell[0]), int(cell[1])
    for i in range(8):
        cx = kx + X[i]
        cy = ky + Y[i]
        if cx >= 1 and cx <= 8 and cy >= 1 and cy <= 8:cando += 1
    return cando

""" def chessKnightMoves(cell):
    r = [2, 3, 4, 6, 8]
    c1 = min(ord(cell[0]) - 97, 104 - ord(cell[0]))
    c2 = min(ord(cell[1]) - 49, 56 - ord(cell[1]))
    print(c1, c2)
    d1 = min(c1, 2);
    d2 = min(c2, 2);
    return r[d1 + d2]
 """
print(chessKnightMoves("a1"))