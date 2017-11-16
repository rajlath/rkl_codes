'''
2
2 2 2 2
2 4
3 2 3 2
2 6 7
'''

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
def lcm(a, b):
    return (a * b) // gcd(a, b)
    
for _ in range(int(input()))    :
    n, x, y, z = [int(x) for x in input().split()]
    allowed = list(set([x, y, z]))
    arr = [int(x) for x in input().split()]
    lcm_arr = arr[0]
    for i in range(1, n):
        lcm_arr = lcm(lcm_arr, arr[i])
    can = False           
    for i in allowed:
        if lcm_arr % i == 0:
            can = True
            
            
                
    
    print(lcm_arr, allowed)    
    print("She can't" if  not can else "She can")    
    
