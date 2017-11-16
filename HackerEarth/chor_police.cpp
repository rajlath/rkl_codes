int main() {
	// fr;
	int T;
	char ch;
	gi(T);
	while (T--) {
		int N, K, res = 0;
		vi chor, police;
		gi(N); gi(K);
		rep(i, N) {
			chor.clear();
			police.clear();
			rep(j, N) {
				cin >> ch;
				assert(ch == 'P' || ch == 'T');
				if (ch == 'P') police.pb(j);
				else chor.pb(j);
			}
			int l = 0, r = 0;
			while (l < chor.size() && r < police.size()) {
				if (Abs(chor[l] - police[r]) <= K) {
					++res; ++l; ++r;
				} else if (chor[l] < police[r]) ++l;
				else ++r;
			}
		}
		pin(res);
	}
	return 0;
}
