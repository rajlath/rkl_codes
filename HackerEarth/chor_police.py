for _ in range(int(input())):
    md, k = [int(x) for x in input().split()]
    res = 0
    for i in range(md):
        carr, parr = [], []
        arr = [(x) for x in input().split()]
        for i, v in enumerate(arr):
            if v == "T":
                carr.append(i)
            else:
                parr.append(i) 
              
        l = 0
        r = 0
        while l < len(carr) and r < len(parr):
            if abs(carr[l] - parr[r]) <= k:
                res += 1
                l += 1
                r += 1
            elif carr[l] < parr[r]: l+= 1
            else: r+= 1
                    
    print(res)                
               
    
