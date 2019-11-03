a = arr1
s = sorted(set(arr2))
def merge(b, free_val):
    i = 0
    m = float('inf')
    r = []
    considered_free = False
    for val in s:
        if not considered_free and free_val <= val:
            while i < len(b) and b[i][0] < free_val:
                m = min(m, b[i][1])
                i += 1
            if i: r.append((free_val, m))
            considered_free = True
        if free_val == val: continue
        while i < len(b) and b[i][0] < val:
            m = min(m, b[i][1])
            i += 1
        if i: r.append((val, m+1))
    if not considered_free:
        while i < len(b) and b[i][0] < free_val:
            m = min(m, b[i][1])
            i += 1
        if i: r.append((free_val, m))
    return r
r = [(float('-inf'), 0)]
for v in arr1:
    r = merge(r, v)
    if not r: return -1
return min(m for _, m in r)