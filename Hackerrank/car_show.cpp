#include <bits/stdc++.h>

using namespace std;

#define ll 			    long long
#define db			    double
#define up(i,j,n)	    for (int i = j; i <= n; i++)
#define down(i,j,n)	    for (int i = j; i >= n; i--)
#define cadd(a,b)	    a = add (a, b)
#define cpop(a,b)	    a = pop (a, b)
#define cmul(a,b)	    a = mul (a, b)
#define pr			    pair<int, int>
#define fi			    first
#define se			    second
#define SZ(x)		    (int)x.size()
#define bin(i)		    (1 << (i))
#define Auto(i,node)	for (int i = LINK[node]; i; i = e[i].next)

template<typename T> inline void cmax(T & x, T y){y > x ? x = y : 0;}
template<typename T> inline void cmin(T & x, T y){y < x ? x = y : 0;}

const int MAXN = 1e6 + 5;
const int oo = 0x3f3f3f3f;

int N, Q, a[MAXN], pos[MAXN], cur, val[MAXN];
ll sum[MAXN];

int get(int L, int R){
	int le = L, ri = R, mi;
	while (le + 1 < ri) {
		mi = (le + ri) >> 1;
		if (val[mi] <= L) le = mi;
		else			ri = mi;
	}
	if (val[ri] <= L) return ri;
	return le;
}

ll calc(ll n){return n * (n + 1) / 2;}

int main(){
	scanf("%d%d", &N, &Q);
	up (i, 1, N) scanf("%d", &a[i]);
	up (i, 1, N) {
		cmax(cur, pos[a[i]] + 1);
		val[i] = cur;
		pos[a[i]] = i;
		sum[i] = i - cur + 1;
		sum[i] += sum[i - 1];
    }
    //up (i,1, N){ cout<<sum[i]<<endl;}
	while (Q--) {
		int le, ri;
		scanf("%d%d", &le, &ri);
		int mi = get(le, ri);
		printf("%lld\n", sum[ri] - sum[mi] + calc(mi - le + 1));
	}
	return 0;
}

//solved by Cydiater