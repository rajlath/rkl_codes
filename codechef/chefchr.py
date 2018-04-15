ss= sorted("chef")
for _ in range(int(input())):
    s = input()
    l = len(s)
    cnt = 0
    if l >= 4:
        limit = l - 4
        for v, i in enumerate(s):
            if v <= limit:
                if i in "chef" :
                    if sorted(s[v:v+4]) == ss:cnt += 1
    if cnt:
        print("lovely {}".format(cnt))
    else:
        print("normal")

