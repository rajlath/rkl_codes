'''
2
5
2 3 1 3 2
6
1 1 2 2 2 1
Output
YES
1 4
2 1
'''
n = int(input())
cl = set()
dic = {}
for i in range(n):
    m = int(input())
    s = list(map(int, input().split()))
    t = []
    sm = sum(s)
    for x in range(m):
        a = sm - s[x]
        if a in cl:
            print('YES')
            print('{} {}'.format(i + 1, x + 1))
            print('{} {}'.format(dic[a][0], dic[a][1]))
            exit()
        dic.update({a: (i+1, x+1)})
        t.append(a)
    for x in set(t):
        cl.add(x)


print('NO')