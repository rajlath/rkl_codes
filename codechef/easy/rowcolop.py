n, q = [int(x) for x in input().split()]
rows = [0] * (n + 1)
cols = [0] * (n + 1)
for _ in range(q):
    comm, index, amt = [x for x in input().split()]
    if comm == "RowAdd":
        rows[int(index)] += int(amt)
    else:
        cols[int(index)] += int(amt)
print(rows, cols)
print(max(rows) + max(cols))
