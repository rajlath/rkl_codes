def merge(intervals):
    out = []
    for i in sorted(intervals, key = lambda x : x[0]):
        if out and (i[0] <= out[-1][1]):
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out.append(i)
            print(out)
    return out




print(merge([[1,3],[2,6],[15,18],[18,20]]))