
 
ins = bin(int(input()))[2:]
x = ins[0]
for i in range(1, len(ins)):
    #t1 = int(px[i])
    #t2 = int(x[i - 1])
    x += str(int(ins[i]) ^ int(x[i - 1]))
    
print(int(x, 2))

