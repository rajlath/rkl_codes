def multipication(a, b):
    cnt = 0
    ans = 0
    anss=[]
    while(b):
        if b%2:
            ans+= a<<cnt
            s = "(" + str(a)+"<<"+str(cnt) +")"
            anss.append(s)
        cnt+=1
        b//=2    
    return anss
    
for _ in range(int(raw_input())):
    a, k, n = [long(x) for x in raw_input().split()]
    
    print(a+int(k*(n-1)))
    
print(64342 * (72178 - 1))    


'''
5
                    mine          should be
4952 64342 72178   4644017486    349050190
23391 28544 16938  483473119    483473119 
60483 54634 92690  5064031309   769064013 
30164 65790 39509  2599261484   -1695705812
69328 34185 30121  1029721528   1029721528
'''
