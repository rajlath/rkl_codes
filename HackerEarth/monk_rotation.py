'''
1
5 2
1 2 3 4 5
'''
for _ in range(int(input())):
    ln, qr = [int(x) for x in input().split()]
    arr = [x for x in input().split()]
    outs= [0] * ln
    for i in range(ln):
        offset = (i + qr)%ln
        outs[offset] = arr[i]
        
    print(" ".join(outs))    
        
        
