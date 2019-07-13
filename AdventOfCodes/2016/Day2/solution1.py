
keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows, cols = 1, 1
code = ''
for line in open("input.txt", "r"):
  for current in line:
    if   current == "U": rows = max(0, rows - 1)
    elif current == "D": rows = min(2, rows + 1)
    elif current == "L": cols = max(0, cols - 1)
    elif current == "R": cols = min(2, cols + 1)
    print(rows, cols)
  code += str(keys[rows][cols])
print(code)

'''
keys = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
x = y = 1
numbers = []

for line in open('input.txt', 'r'):
    for c in line:
        if c == 'U':
            y = max(0, y - 1)
        elif c == 'D':
            y = min(2, y + 1)
        elif c == 'L':
            x = max(0, x - 1)
        elif c == 'R':
            x = min(2, x + 1)
    numbers.append(str(keys[y][x]))

print(''.join(numbers))
'''