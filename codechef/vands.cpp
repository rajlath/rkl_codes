const int MAX_N = (int)3e5 + 123;
const double eps = 1e-6;
const int inf = (int)2e9 + 123;

using namespace std;

bool ok(string &a, string &b) {
    if (sz(a) == sz(b)) {
        int cnt = 0;
        for (int i = 0; i < sz(a); i++)
            cnt += (a[i] != b[i]);
        return (cnt <= 1);
    }
    bool ok = 0;
    if (sz(a) > sz(b))
        swap(a, b), ok = 1;
    int cnt = 0;
    for (int i = 0, j = 0; i < sz(a); i++) {
        if (b[j] != a[i]) {
            if (cnt) {
                if (ok)
                    swap(a, b);
                return 0;
            }
            cnt++;
            j++;
        }
        if (j == sz(b) || b[j] != a[i]) {
            if (ok)
                swap(a, b);
            return 0;
        }
        assert(b[j] == a[i]);
        j++;
    }
    if (ok)
        swap(a, b);
    return 1;
}

int main() {

    ios_base :: sync_with_stdio(NULL), cin.tie(NULL);
    string s, t;
    int ans = 0;
    cin >> s >> t;
    ans = ok(s, t)
    cout << ans;
    return 0;
}