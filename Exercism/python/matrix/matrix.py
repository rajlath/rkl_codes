class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in y.split()] for y in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        mats = list(zip(*self.matrix))
        #print(mats)
        return list(mats[index-1])

print(Matrix("89 1903 3\n18 3 1\n9 4 800").column(2))