'''
'''
def hash_table(s):
    hash = 1
    for i in s:
        hash *= (ord(i) - ord('a') + 1)
    return hash

def mid_hash_table(s,a,b):
    return (s // ((ord(a) - ord('a'))+1)) * (ord(b) - ord('a')+1)

for _ in range(int(input())):
    s = input()
    l = len(s)
    t = input()
    sh = hash_table(s)
    st = hash_table(t[:l])
    #print(sh, st)
    maxs = 0
    dict = {}
    ans  = -1
    for i in range(1, len(t)-l):
        curr = t[i:i+l]
        mhash =  mid_hash_table(st,t[i-1], t[i+l])
        if mhash == sh:
            dict[curr] = dict.get(curr, 0) + 1
            if dict[curr] > maxs:
                maxs = dict[curr]
                ans  = curr
        st = mhash
    print(ans)





