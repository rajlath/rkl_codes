valid = []

def check(src,des):
    for j in range(26):
        if valid[j][src] == True:
            c = valid[j][des]
            valid[j].append(True)
            if not c: check(j, des)
        if valid[des][j] == True:
            c = valid[src][j]
            valid[src][j] = True
            if not c: check(src, j)

nb_pair, nb_words = [int(x) for x in input().split()]
valid = [[False for _ in range(26)] for _ in range(26)]
for i in range(26): valid[i][i] = True
for i in range(nb_pair):
    f, t = input().split()
    f  =  ord(f) - ord('a')
    t  =  ord(t) - ord('a')
    c  =  valid[f][t]
    valid[f][t] = True
    if not c: check(f, t)
for i in range(nb_words):
    is_ok = True
    old, new = [x for x in input().split()]
    if len(old) != len(new):
        print("no")
        continue
    for j in range(len(old)):
        if not valid[ord(old[j]) - ord('a')][ord(new[j]) - ord('a')]: is_ok = Fales
    print(["no", "yes"][is_ok == True])








