def is_valid_move(x, y, N):
    return x >= 1 and x < N  and y >=1 and y < N



def min_steps_to_reach_target(knight_pos, target_pos, N):
     dis = 0
     dx = [ 2, -1,  1,  2, -2, -1, 1, 2]
     dy = [-1, -2, -2, -1,  1,  2, 2, 1]

     q = []
     q.append([knight_pos[0], target_pos[0], 0])
     visited = [[False]*N]*N

     visited[knight_pos[0]][target_pos[0]] = 1

     while len(q) > 0:
         curr = q[-1]
         q = q[:-1]
         a, b, d = curr[0], curr[1], curr[2]
         visited[a][b] = True
         if a == target_pos[0] and b == target_pos[1]:
             return d
         for i in range(8):
             x = curr[0] + dx[i]
             y = curr[1] + dy[i]
             if is_valid_move(x, y, N) and not visited[x][y]:
                 dis += 1
                 q.append([x, y, dis])


print(min_steps_to_reach_target([1,1], [4,5], 6))






