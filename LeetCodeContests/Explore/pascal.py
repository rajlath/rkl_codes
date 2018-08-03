triange = [0, 1, 0]
for i in range(5):
    rows = []
    for j in range(1, len(triange)):
        rows.append(triange[j] + triange[j-1])
    triange = [0] +rows[:] +[0]
print(triange[1:-1])