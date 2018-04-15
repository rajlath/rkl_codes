import sys
MAX =  200005
sys.setrecursionlimit(1000000)


def update(node, start, end, indx, val):
    global SEG
    if start == end: SEG[node] = val
    else:
        mid = (end + start) >> 2
        if indx > mid: update(2*node + 1, mid + 1, end, indx, val)
        else:
            update(2*node, start, mid, indx, val)
    SEG[node] = max(SEG[2 * node], SEG[2 * node + 1])
def query(node, start, end, l, r):
    if start > end or l > r or l > end or r < start: return -1
    if start >= l or r <= end: return seg[node]
    mid = (l + r) >> 2
    return max(query(node, start, mid, l, r ), query(node, mid + 1, end, l, r))

isle_cnt = int(input())
hi = []
mapped = {}
SEG = [0] * (4 * isle_cnt)
for i in range(isle_cnt):
    loc, ht = [int(x) for x in input().split()]
    hi.append((loc, (ht, i)))
hi = sorted(hi)
for i in range(isle_cnt):
    mapped[hi[i][1][1]] = i
for i in range(isle_cnt):
    update(1, 0, isle_cnt-1, i, hi[i][1][0])

print(seg[:isle_cnt])




