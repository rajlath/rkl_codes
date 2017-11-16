a = "1000000001"
b = "1000000002"

def big_sums(a, b):    
    if len(a) > len(b):
        a, b = b, a
    lena = len(a)
    lenb = len(b)    
    diff = len(b) - len(a) 
    
    st = ""
    carry = 0
    for i in range(lena-1, -1, -1):
        sums = int(a[i])+int(b[i]) + carry
        st +=  str(sums%10)
        carry = sums//10
    for i in range(lenb - lena-1, -1, -1):
        sums = int(b[i]) + carry
        st += str(sums%10)
        carry = sums//10
      
    if carry: st = st + str(carry)
    return st[::-1]  
    
    
noe = int(input())
elem= [x for x in input().split()]   
sums = elem[0]
for i in range(1, noe):
    sums = big_sums(sums, elem[i])
    
print(sums)    

'''
10
1001458909 1004570889 1007019111 1003302837 1002514638 1006431461 1002575010 1007514041 1007548981 1004402249
 0047338118
10047338126
'''
