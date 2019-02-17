def saddle_points(matrix):
    points = set()
    if matrix == []:return set([])
    nb_rows = len(matrix)
    nb_cols = len(matrix[0])


    for r in range(nb_rows):
        if len(matrix[r])  != nb_cols:
            raise ValueError("Wrong matrix")
        max_in_row = max(matrix[r])
        for r1, v1 in enumerate(matrix[r]):
            if v1 == max_in_row:
                col = [matrix[x][r1] for x in range(nb_rows)]
                if min(col) == max_in_row:
                    points.add((r+1, r1+1))
    return points

print(saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]]))


