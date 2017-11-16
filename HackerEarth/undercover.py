'''
SAMPLE INPUT 
3
5
12
41
SAMPLE OUTPUT 
3
9
19
'''

for _ in xrange(input()):
    n = input()
    nb = bin(n)[2:]
    nb1 = nb[1:] + nb[0]
    print(int(nb1,2))
    
   
            
    
