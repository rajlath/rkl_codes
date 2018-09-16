m1 = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
def find_in_sorted_matrix(ml, v):
    found = False
    row = 0
    col = len(ml[0]) - 1
    while row < len(ml) and col >= 0:
        if ml[row][col] == v:
            found = True
            break
        elif ml[row][col] > v:
            col -= 1
        else:
            row += 1
    return found

print(find_in_sorted_matrix(m1, 15))
