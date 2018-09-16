file = open("rosalind_cons.txt", "r")
file_ans = open("rosalind_cons_ans.txt", "w")
curr = ""
cons = []
for lines in file:
    if lines.startswith(">R"):
        if curr:
            cons.append(curr)
            curr = ''
    else:
        curr += lines.strip()
cons.append(curr)
m = len(cons[0])
n = len(cons)


profile = [[0 for i in range(m)] for j in range(4)]
for i in range(n):
    for j in range(m):
        profile[0][j] += cons[i][j] == "A"
        profile[1][j] += cons[i][j] == "C"
        profile[2][j] += cons[i][j] == "G"
        profile[3][j] += cons[i][j] == "T"
alls = "ACGT"
tran = list(zip(*profile))
ans  = ''
for i in tran:
    ans +=  alls[i.index(max(i))]
file_ans.write(ans)
file_ans.write("\n")
file_ans.write("A: {}".format(" ".join(map(str,profile[0]))))
file_ans.write("\n")
file_ans.write("C: {}".format(" ".join(map(str,profile[1]))))
file_ans.write("\n")
file_ans.write("G: {}".format(" ".join(map(str,profile[2]))))
file_ans.write("\n")
file_ans.write("T: {}".format(" ".join(map(str,profile[3]))))
file_ans.write("\n")
file.close
file_ans.close







