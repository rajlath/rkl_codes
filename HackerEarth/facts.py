def zeroes1(value):
    result = 0;

    d = 5;

    while (d <= value): 
        result += value // d; # integer division
        d *= 5;

    return result; 
print(zeroes1(625))    
 

def zeroes(num)  :
    print(num // 5 + num //25)
    
zeroes(625)    
