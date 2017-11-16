'''
1
5 4 10
4 2 4 6 1
2 1 8 5

4
'''

for _ in range(int(input())):
    n, m, x = [int(x) for x  in input().split()]
    stk1 = [int(x) for x  in input().split()]
    stk2 = [int(x) for x  in input().split()]
    stk1r = stk1[::-1]
    stk2r = stk2[::-1]
    fsum = 0
    i = 0
    while len(stk1r)>0 and fsum + stk1r[-1] <= x:
        fsum += stk1r.pop()
        i += 1
    cnt = i
    print(fsum, i)
    j = 0
    while j < m and i >= 0:
        fsum += stk2r.pop()        
        j += 1
        print(fsum, j, i)
        while fsum > x and i >= 0:
            fsum -= stk1[i-1]            
            i -= 1
          
    if fsum <= x and (i + j) < cnt:
        cnt = i + j
    print(cnt)                 
        
