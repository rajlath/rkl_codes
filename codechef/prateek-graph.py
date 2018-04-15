'''
	int t; cin >> t;
	while(t--) {
		int n, m; cin >> n >> m;
		int deg[n+1];
		memset(deg, 0, sizeof deg);
		forn(i, m){
			int x, y; cin >> x >> y;
			deg[x]++; deg[y]++;
		}
		int cnt;
		cnt = 0;
		for1(i, n){
			if(deg[i] % 2 == 0) cnt++;
		}
		if(cnt % 2 == 0) cout << "Even\n";
		else cout << "Odd\n";
	}
'''
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    deg = [0]*(n+1)
    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        deg[x]+=1
        deg[y]+=1
    cnt = sum([1 for x in deg if x%2==0])
    print(["Odd", "Even"][cnt & 1])
