#include<stdio.h>
#define MAX 10000
#define ll long long
int a[MAX];
int main() {
    int n ,m ,i ,ax ,bx ,cx ,k ,j;
    ll x;
    scanf("%d %d" ,&n ,&m);
    for(i = 0  ; i < n ; i++){
        scanf("%lld" ,&x);
        a[x % m]++;
    }
    // 3 same
    ll ans = 0LL;
    for(i = 0 ; i < m ; i++) {
        ax = a[i];
        bx = ax - 1;
        cx = bx - 1;
        if(cx <= 0) continue;
        if(3 * i % m == 0)  ans += 1LL * ax * bx *cx / 6;
    }
    // 3 diff
    for(i = 0 ; i < m ;i++){
        for(j = i + 1 ; j < m ; j++){
            k = (3 * m - i - j)%m;
            if(k <= j)  continue;
            ans += 1LL * a[i] * a[j] * a[k];
        }
    }
    // 2 + 1
    for(i = 0 ; i < m ; i++){
        for(j = 0 ; j < m ; j++){
            if(i == j)  continue;
            if((2 * i + j )%m == 0){
                ans += 1LL * a[i] * (a[i] - 1) / 2 * a[j];
            }
        }
    }
    printf("%lld" ,ans);
    return 0;
}
