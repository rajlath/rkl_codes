class Solution {
public:
typedef long long ll;

bool isPalindrome(ll n) {
    string s = to_string(n);
    for (int i = 0, j = (int)s.size() - 1; i <= j; i++, j--) {
    if (s[i] != s[j]) return false;
    }
    return true;
}

int numPalindromes(ll n) {
    int res = 0;
    for (ll i = 1; i < 10000000; i++) {
    ll tmp = i;
    ll even = i;
    while (tmp) {
        even = 10 * even + (tmp % 10);
        tmp /= 10;
    }
    ll odd = i;
    tmp = i / 10;
    while (tmp) {
        odd = 10 * odd + (tmp % 10);
        tmp /= 10;
    }
    if (odd * odd > n) break;
    if (even * even <= n && isPalindrome(even * even)) res++;
    if (isPalindrome(odd * odd)) res++;
    }
    return res;
}

int superpalindromesInRange(string A, string B) {
    ll a = stoll(A);
    ll b = stoll(B);
    return numPalindromes(b) - numPalindromes(a - 1);
}
};class Solution {
public:
typedef long long ll;

bool isPalindrome(ll n) {
    string s = to_string(n);
    for (int i = 0, j = (int)s.size() - 1; i <= j; i++, j--) {
    if (s[i] != s[j]) return false;
    }
    return true;
}

int numPalindromes(ll n) {
    int res = 0;
    for (ll i = 1; i < 10000000; i++) {
    ll tmp = i;
    ll even = i;
    while (tmp) {
        even = 10 * even + (tmp % 10);
        tmp /= 10;
    }
    ll odd = i;
    tmp = i / 10;
    while (tmp) {
        odd = 10 * odd + (tmp % 10);
        tmp /= 10;
    }
    if (odd * odd > n) break;
    if (even * even <= n && isPalindrome(even * even)) res++;
    if (isPalindrome(odd * odd)) res++;
    }
    return res;
}

int superpalindromesInRange(string A, string B) {
    ll a = stoll(A);
    ll b = stoll(B);
    return numPalindromes(b) - numPalindromes(a - 1);
}
};

from math import sqrt

class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        l = int(L)
        r = int(R)
        l_below = int(sqrt(l) + 0.9)
        r_upper = int(sqrt(r))

        l_s = str(l_below)
        l_p = min(10 ** (len(l_s) // 2), int(l_s[:(len(l_s) + 1) // 2]))

        r_s = str(r_upper)
        r_p = max(int(r_s[:(len(r_s) + 1) // 2]), 10 ** (len(r_s) // 2))
        count = 0
        print(l_p, r_p)
        for i in range(l_p, r_p + 1):
            i_s = str(i)
            i2 = int(i_s + i_s[-2::-1])
            #print('try', i2)
            v = i2 * i2
            if l <= v <= r:
                #print('check',v,'=',i2,'**2')
                v_s = str(v)
                if v_s == v_s[::-1]:
                    count += 1
            i3 = int(i_s + i_s[::-1])
            #print('try', i3)
            v = i3 * i3
            if l <= v <= r:
                v_s = str(v)
                #print('check',v,'=',i3,'**2')
                if v_s == v_s[::-1]:
                    count += 1
        return count

        typedef long long ll;
class Solution {
public:
    int superpalindromesInRange(string L, string R) {
        ll l=stoll(L),r=stoll(R);
        int ans=0;
        for(int n=1;n<100000;n++)
            for(int p=0;p<2;p++){
                if(n>=10000&&p==0)continue;
                ll t=n,palin=n;
                if(p==1)t/=10;
                while(t>0){
                    palin=palin*10+t%10;
                    t/=10;
                }
                palin*=palin;
                if(palin<l||palin>r)continue;
                string s=to_string(palin);
                bool ok=true;
                for(int i=0;i<s.size()/2;i++)
                    if(s[i]!=s[s.size()-1-i]){
                        ok=false;
                        break;
                    }
                if(ok)ans++;
            }
        return ans;
    }
};