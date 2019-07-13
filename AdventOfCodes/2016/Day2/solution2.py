
keys = [[' ', ' ', '1', ' ', ' '],[' ', '2', '3', '4', ' '],['5', '6', '7', '8', '9'],[' ', 'A', 'B', 'C', ' '],[' ', ' ', 'D', ' ', ' ']]
row, curr_row, col, curr_col = 2, 2, 0, 0
code = ''
for line in open("input.txt", "r"):
  for current in line:
    curr_row = row
    curr_col = col
    if   current == "U": curr_row = max(0, row - 1)
    elif current == "D": curr_row = min(4, row + 1)
    elif current == "L": curr_col = max(0, col - 1)
    elif current == "R": curr_col = min(4, col + 1)
    if keys[curr_row][curr_col] != " ":
      row = curr_row
      col = curr_col
  code += str(keys[row][col])
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