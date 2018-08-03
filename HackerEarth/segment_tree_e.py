def build_BIT(val, start, end, )
noe, noq = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
Tree = [0] * (2 * noe)
for i in range(noe):
    Tree[noe + i] = arr[i]
for i in range(noe-1, -1, -1):
    Tree[i] = Tree[i<<1] + Tree[i<<1 | 1]
for i in range(noq):
    c, l, r = [x for x in input().split()]
    l, r = int(l)-1, int(r) - 1
    if c == "q":
        l += noe
        r += noe
        res = 0
        while l < r:
            if l & 1:
                l += 1
                res += Tree[l]
            if r & 1:
                r -= 1
                res += Tree[r]
            l >>= 1
            r >>= 1
        print(res)
    if c == "u":
        Tree[l + noe] = r
        l += noe
        i = l
        while i > 1:
            Tree[i>>1] = Tree[i] + Tree[i^1]
            i >>= 1










