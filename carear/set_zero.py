def set_zeros(mats):
    '''
    for a mats if any rows or cols has a zero in it
    make entire rows or cols zero.

    ins : a mats
    outs: a mats
    '''
    row_having_0 = []
    col_having_0 = []
    for i in range(len(mats)):
        for j in range(len(mats[0])):
            if mats[i][j]==0:
                row_having_0.append(i)
                col_having_0.append(j)
    print(row_having_0, col_having_0)
    for i in range(len(mats)):
        for j in range(len(mats[0])):
            if i in row_having_0 or j in col_having_0:
                mats[i][j]=0
    return mats


print(set_zeros([[1,0,3],[4,5,6],[0,8,9]]))




