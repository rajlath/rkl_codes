row, col = [int(x) for x in input().split()]
rects = []
star_rows = ''
first_col, last_col = col, 0
for i in range(row):
    curr = input()
    rects.append(curr)
    if "*" in curr:
        star_rows += "*"
        if curr.index("*") < first_col:
            first_col = curr.find("*")
        if curr.rindex("*") > last_col:
            last_col = curr.rfind("*")
    else:
        star_rows += "."

first_row, last_row = star_rows.index("*"), star_rows.rindex("*")
for i in rects[first_row: last_row + 1]:
    print(i[first_col:last_col+1])