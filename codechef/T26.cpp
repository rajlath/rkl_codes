ll fast_exp(int base, int exp) {
    ll res=1;
    while(exp>0) {
       if(exp%2==1) res=(res*base)%MOD;
       base=(base*base)%MOD;
       exp/=2;
    }
    return res;
}

void main()
{
    int b = 123456789;
    int e = 987654321;
    cout<<fast_exp(b, e)<<endl;
}