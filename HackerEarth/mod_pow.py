'''
modpow(ll a,ll n,ll temp){ll res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;}
'''

def modpow(a, n, mods=10e9+7):
    res = 1
    y = a
    while n > 0:
        if n & 1: res = (res * y)%mods
        y = (y* y)%mods
        n//=2
    return int(res%mods)

print(modpow(25,2612))            
