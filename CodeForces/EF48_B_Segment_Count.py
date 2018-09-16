
lena, lenb, noq = [int(x) for x in input().split()]
a = input()
b = input()
'''
for i in range(noq):
    s, e = [int(x)-1 for x in input().split()]
    curr = a[s:e+1]
    #print(curr)
    ans = sum(1 for _ in re.finditer('(?='+b+')', curr))
    print(ans)
'''
cnts = [0] * lena
for i in range(lena):
    cnts[i] += a[i:i+lenb] == b
for i in range(noq):
    s, e = [int(x) for x in input().split()]
    s, e = s-1, e - lenb + 1
    ans = 0
    if s < e :ans = (sum(cnts[s:e]))
    print(ans)

