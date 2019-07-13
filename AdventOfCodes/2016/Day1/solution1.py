'''
data = open('input1.txt', "r").readline().strip().split(", ")
print(data)
x, y, current = 0, 0, 0
for move in data:
  change, steps = move[0], move[1:]
  print(change, steps)
  steps = int(steps)
  if change == "L":
    current = 3 if current == 0 else current - 1
  if change == "R":
    current = 3 if current == 0 else current + 1
  if   current == 0: y -= steps
  elif current == 1: x += steps
  elif current == 2: y += steps
  elif current == 3: x -= steps
print(abs(x) + abs(y))
'''
x = y = direction = 0
moves = open('input1.txt', 'r').readline().strip().split(', ')

for move in moves:
    if move[0] == 'L':
        if direction == 0:
            direction = 3
        else:
            direction -= 1
    elif move[0] == 'R':
        if direction == 3:
            direction = 0
        else:
            direction += 1

    dist = int(''.join(move[1:]))
    if direction == 0:
        y -= dist
    elif direction == 1:
        x += dist
    elif direction == 2:
        y += dist
    elif direction == 3:
        x -= dist

print(abs(x) + abs(y))
input()