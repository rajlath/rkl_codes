'''
 4
3
5 10 -5
2
8 -8
3
10 2 -5
4
-2 -1 1 2
'''
for _ in range(int(input())):
    noa = int(input())
    ast = [int(x) for x in input().split()]
    ans = []

    for i in range(len(ast)-1, -1, -1):
        if ast[i] < 0:
           if ast[i-1]< 0:
               ans.append(ast[i-1])
               ans.append(ast[i])
               continue
           else:
               aa = abs(ast[i])
               ab = abs(ast[i-1])
               if aa == ab:
                   pass
               elif aa > ab:
                   ans.insert(0,ast[i])
               else:
                   ans.insert(0, ast[i-1])
    print(ans)






