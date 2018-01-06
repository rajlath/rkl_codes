def levenshtein_dist(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)
    cols  = [0]*(lstr1+1)
    for i in range(1, lstr1+1, 1):
        cols[i] = i
    for x in range(1, lstr2+1, 1):
        cols[0] = x
        lastkey = x - 1
        for y in range(1, lstr1+1, 1):
            oldkey = cols[y]
            incr = 0
            if str1[y - 1] != str2[x - 1]:
                incr = 1
            cols[y] = min(cols[y]+1, cols[y-1]+1, lastkey+incr)
            lastkey = oldkey
    return cols[lstr1]

print(levenshtein_dist("Python", "Peithen"))






