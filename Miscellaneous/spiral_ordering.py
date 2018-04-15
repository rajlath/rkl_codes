def matrix_in_spiral_order(square_matrix):
    k_shift =[[0, 1], [1, 0], [0, -1], [-1, 0]]
    dirs, x, y = 0, 0, 0
    lens = len(square_matrix)
    spiral_ordering = [[0 for x in range(lens)] for y in range(lens)]
    for i in range(lens*lens):
        spiral_ordering[x][y] = square_matrix[x][y]
        square_matrix[x][y] = 0
        next_x = x + k_shift[dirs][0]
        next_y = y + k_shift[dirs][1]
        print(x, y)
        if next_x < 0 or next_x >= lens or next_y < 0 or next_y >= lens or square_matrix[next_x][next_y]==0:
            print("Failed :{} {}".format(x, y))
            dirs = (dirs + 1) % 4
            next_x = x + k_shift[dirs][0]
            next_y = y + k_shift[dirs][1]
        x = next_x
        y = next_y






    return spiral_ordering

print(matrix_in_spiral_order([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))


