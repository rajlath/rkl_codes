def login_attemp(n, s, a):
    asize = len(a)
    b     = 0
    t     = []
    for i in s:
        curr = ''
        lens = len(i)
        for j in range(lens):
            curr += a[b + j]
            if b + lens - 1 < asize:
                if i == curr:
                    b += lens
                    t.append(i)
    if b == asize :
        for i in t:
            print(s[i])



    '''
    for i in range(n):
        comp = ''
        size = len(s[i])
        for p in range(size):
            print(b)
            comp += a[b + p]
            print(comp)
            if b + size - 1 < asize:
                if s[i] == comp:
                    b+=size
                    t.append(i)
                    i=-1
    '''
    if b==asize:
        for i in range(len(t)):
            print(s[t[i]], end=" ")
    else:
        print("WRONG PASSWORD")
    return None
'''
for _ in range(int(input())):
    n = int(input())
    s = [x for x in input().split()]
    a = input()
'''
login_attemp(3, ["ab", "abcd", "cd"], "abcd")










