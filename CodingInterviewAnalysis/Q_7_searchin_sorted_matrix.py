'''
Question 7 In a 2-D matrix, every row is increasingly sorted from left to right, and the last number
in each row is not greater than the first number of the next row. A sample matrix follows.
Please implement a function to check whether a number is in such a matrix or not.
It returns true if it tries to find the number 7 in the sample
matrix, but it returns false if it tries to find the number 12.
'''
from random import randint, choice

def search_in_matrix(matrix, look_for):
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    rite = (rows * cols) - 1
    while left <= rite:
        mids = (rite - left) // 1
        r = mids // cols
        c = mids %  cols
        curr = matrix[r][c]
        if curr == look_for:
            return True
        else:
            if curr > look_for:
                rite = mids - 1
            else:
                left = mids + 1
    return False

#create a 1D array of lens = m * n int numbers which are sorted.
#ranges is the max value that will be in this arr
def create_1D_arr(lens, ranges)    :
    arr =  [randint(1, ranges) for _ in range(lens)]
    arr.sort()
    return arr


#a 1D arr is created using create_id_function
#m and n are the row len and col len of the matrix
def create_matrix_from_1D_arr(m, n, arr_1D):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    indx = 0
    for i in range(m):
        for j in range(n):
            matrix[i][j] = arr_1D[indx]
            indx += 1
    return matrix

m, n = randint(1, 10), randint(1, 10) # nos of rows = m and nos of cols = n
rng  = int(10 ** (randint(1, 5)))
arr_1D = create_1D_arr(m * n, rng)
#print(arr_1D[:10])
matrix = create_matrix_from_1D_arr(m, n, arr_1D)
#print(matrix)
to_search = choice(arr_1D)
search_invalid = to_search + rng  # a value that will not be found in matrix
print(search_in_matrix(matrix, to_search))       # should display True
print(search_in_matrix(matrix, search_invalid))  # should display False







