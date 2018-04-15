#include <cstdio>
#include <vector>

using namespace std;

const int N = 500;

int n, m, mark[N], cnt = 0;
vector<int> g[N];

void dfs(int u);

int main() {
	scanf("%d%d", &n, &m);
	for (; m--; ) {
		int u, v;
		scanf("%d%d", &u, &v);
		u--;
		v--;
		g[u].emplace_back(v);  //same as push_bak: adds elements to the end of the container
	}
	for (int u = 0; u < n; u++) {
		cnt = 0;
		fill(mark, mark + n, 0);
		dfs(u);
		for (int v = 0; v < n; v++) {
			if (!mark[v]) {
				dfs(v);
			}
		}
		if (cnt <= 1) {
			puts("YES");
			return 0;
		}
	}
	puts("NO");
	return 0;
}

void dfs(int u) {
	mark[u] = 1;
	for (auto v : g[u]) {
		if (!mark[v]) {
			dfs(v);
		} else if (mark[v] == 1) {
			cnt++;
		}
	}
	mark[u] = 2;
}