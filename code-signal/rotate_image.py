def rotateImage(a):
    tuples = zip(*a[::-1])
    return [list(i) for i in tuples]











print(rotateImage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))