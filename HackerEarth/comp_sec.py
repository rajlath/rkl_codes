N = 8
st = [''] * N

def solve(x):
    global k
    if x == k:        
        print("".join(st))
        return
    st[x] = '1'
    solve(x + 1)
    st[x] = '5'
    solve(x + 1)
    st[x] = '7'
    solve(x + 1)
    st[x] = '9'
    solve(x + 1)   
        

n = int(input())
for k in range(1,  n):
    solve(0)
 



