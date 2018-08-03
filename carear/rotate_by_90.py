def rotate_by_90(mats):
    '''
    rotate a matrix by 90 degree
    top goes to right
    right to bottom
    bottom to left
    left to top

    ins : a matrix
    outs: rotated matrix
    '''
    for i in range(0, len(mats)//2):
        first = i
        last  = len(mats) - 1 - i
        for j in range(first, last):
            offset = i - first
            top = mats[first][i]
            mats[first][i] = mats[last-offset][first]
            mats[last-offset][first] = mats[last][last-offset]
            mats[last][last-offset] = mats[i][last]
            mats[i][last]=top
    return mats

print(rotate_by_90([[1,2,3],[4,5,6],[7,8,9]]))




