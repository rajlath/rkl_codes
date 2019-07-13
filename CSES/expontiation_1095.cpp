#include <iostream>

using namespace std;

typedef long long ll;

const int M = 1000000007;

int power(int a, int n, int mod)
{
    long long power = a;
    long long result = 1;

    while (n)
    {
        if (n & 1) result = (result * power) % mod;
        power = (power * power) % mod;
        n >>= 1;
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        int b, c, d;
        cin >> b >> c >> d;
        int e = power(c, d, M-1);

        int answer = power(b, e, M);

        cout <<answer << endl;
    }
}
