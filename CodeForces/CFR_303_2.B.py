current = 0
answer  = []
s = [x for x in input()]
t = [x for x in input()]
for x, y in zip(s, t):
    if x != y:
        answer.append([x, y][current])
        current = 1 - current
    else:
        answer.append(x)
print("impossible" if current else ''.join(answer))        
