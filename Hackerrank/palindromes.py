from collections import Counter
def can_be_palindromes(s):
    oddlen = len(s)%2
    sc = Counter(s)
    mids = 0
    for i in sc:
        if sc[i]%2:
            if not oddlen:
                return ""
            else:
                mids += 1
                if mids>1:
                    return ""
    chrs = sorted(sc.keys())

    ans  = ["*"]*len(s)
    l=0
    r=-1
    for c in chrs:
        if sc[c]%2==1:
            ans[len(s)//2] = c
        for i in range(sc[c]//2):
            ans[l]=c
            ans[r]=c
            l+=1
            r-=1
    return "".join(ans)

lens = int(input())
s, q = [x for x in input().split()]
for _ in range(int(q)):
    a, b = [int(x) for x in input().split()]
    curr = s[a-1:b]
    ans  = can_be_palindromes(curr)
    s = s[:a-1] + ans+s[b:]
print(s)








