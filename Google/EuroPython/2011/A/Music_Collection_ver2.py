
def main(array):
    if len(array) == 1:
        return ['']

    sub = {}
    for name in array:
        l = len(name)
        x = name.lower()
        was = set()
        for p1 in range(l - 1):
            for p2 in range(p1 + 1, l):
                s = x[p1:p2]
                if s in was:
                    continue
                else:
                    was.add(s)
                try:
                    sub[s] += 1
                except KeyError:
                    sub[s] = 1
    res = [x[0] for x in sub.items() if x[1] == 1]
    res.sort(key=lambda s: len(s))

    out = []
    for name in array:
        matching = []
        name_lc = name.lower()
        for s in res:
            if s in name_lc:
                matching.append(s)
#		print name, matching

        if matching:
            min_len = len(matching[0])
            xxx = filter(lambda s: len(s) ==  min_len, matching)
            item = sorted(xxx)[0].upper()
            out.append(item)
        else:
            out.append(None)
    return out


if __name__ == '__main__':
    import sys
    out = open("out_small.txt", "w")
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        a = "Case #%d:" % (i + 1)
        print(a, file=out)
        songs = []
        for j in range(N):
            songs.append(sys.stdin.readline())
        res = main(songs)
        for s in res:
            ans = [":", s][s is not None]
            print(ans, file=out)
            #print ('"%s"' % s if s is not None else ':', file=out)
