#copied
int main() {
    ios_base::sync_with_stdio(false);  cin.tie(0); // for faster input and output in c++
    int n,i,j,x,y;
    cin >> n;
    vii a; // taking an vectors of pairs
    FORK(i,1,n)
    {
        cin >> x >> y;
        a.pb(mp(x+y,i));
    }
    sort(ALL(a));  
    FOR(i,sz(a))
    cout << a[i].se << " "; 
    return 0;
}
