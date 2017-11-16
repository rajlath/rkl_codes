#include <bits/stdc++.h>
 
using namespace std;
 
#define N 8
 
int k;
char str[N + 2];
 
void solve(int x){
	if (x == k){
		str[x] = '\0';
		printf("%s\n", str);
		return;
	}
 
	str[x] = '1';
	solve(x + 1);
	str[x] = '5';
	solve(x + 1);
	str[x] = '7';
	solve(x + 1);
	str[x] = '9';
	solve(x + 1);
}
 
int main(){
	int n;
 
	scanf("%d", &n);
 
	for (k = 1; k <= n; k++){
		solve(0);
	}
 
	return 0;

