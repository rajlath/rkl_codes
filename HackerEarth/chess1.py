from itertools import product
def knight_moves(position, matrix):
    x, y = position[0], position[1]
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < matrix and y < matrix]
    return moves


q = []
move = 0
position = [1, 1]
q.append(position)
while len(q) > 0:
    curr = q.pop()
    moves = knight_moves(curr, 8)
    move += len(moves)
    q.append(moves)
print(move)
