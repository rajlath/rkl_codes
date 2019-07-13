from math import floor, ceil
plain = input()
plain = "".join(plain.split())
lens = len(plain)
rows = floor(lens ** 0.5)
cols = ceil(lens ** 0.5)
if (rows - 1) * cols >= lens:
    rows -=1
elif cols - 1 * rows >= lens:
    cols -=1
elif cols - 1 * rows - 1 >= lens:
    rows -= 1
    cols -= 1
ans = [["" for x in range(cols+1)] for x in range(rows+1)]
x = 0
for i in range(rows):
    for j in range(cols):
        try:
            ans[i][j] = plain[x]
            x += 1
        except IndexError:
            break
ans = ["".join(x) for x in (list(zip(*ans)))]
print(*ans)
