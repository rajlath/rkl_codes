k = 3
file = open("graph_015_input.txt", "r")
ids = []
txt=[]
for lines in file:
    if lines.startswith(">R"):
        ids.append(lines.strip())
    else:
        txt.append(lines.strip())
print(ids, txt)
ans = []
print(txt[0][:-k - 1])
for i in range(len(ids)):
    curr = txt[i][:-k-1]
    for j in range(i+1, len(txt))        :
        if txt[j].startswith(curr):
            entry = ids[i][1:] +" "+ids[j][1:]
            if entry not in ans:ans.append(entry)
for i in ans:
    print(i)








