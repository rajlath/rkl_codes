for _ in range(int(input())):
    n = int(input())
    bit_count = {}
    for i in range(n):
        pos = 0
        x = int(input())
        while x:
            bit_count[pos] = bit_count.get(pos, 0) + x%2
            pos += 1
            x//=2
    bit_count = sorted(bit_count.items(), key=lambda x: (x[1],x[0]), reverse=True) 
    max_cnt = bit_count[0][1]
    min_ind = bit_count[0][0]
    
    for i, v in bit_count:
        if v == max_cnt:
            min_ind = min(min_ind, i)
        else:
            break    
    print(min_ind)        
     
    
