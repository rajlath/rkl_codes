
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