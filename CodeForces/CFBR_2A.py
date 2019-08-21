lens = int(input())
scores = {}
board  = []
for i in range(lens):
    a, b = input().split()
    scores[a] = scores.get(a, 0) + int(b)
    board.append((a, scores[a]))
maxs = max(scores.values())
for i, j in board:
    if scores[i] == maxs and int(j) >= maxs:
        print(i)
        break
