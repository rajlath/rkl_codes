'''
2
7
DDKDKDK
6
DKDKKD
'''
for _ in range(int(input())):
    total_count = int(input())
    arranged = input()
    
    total_knights = arranged.count("K")
    now_in  = arranged[:total_knights].count("K")
    
    indx1 = 0
    tk = indx2 = total_knights
    while indx1 < total_count:
        now_in -= [0,1][arranged[indx1] == 'K']        
        now_in += [0,1][arranged[indx2%total_count] == 'K']
        tk = min(tk, total_knights - now_in)
        indx1+=1
        indx2+=1
    print(tk)    
    
