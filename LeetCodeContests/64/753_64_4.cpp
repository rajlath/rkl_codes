/*
753. Cracking the Safe My SubmissionsBack to Contest

Difficulty: Hard
There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits
 0, 1, ..., k-1.
You can keep inputting the password, the password will automatically be matched against the last n digits entered.
For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.
Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
Note:
n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.
*/
class Solution {
public:
    int kn, n, k;
    char c[10000];
    bool vis[10000];
    void dfs(int x, int h)
    {
				// printf("%s\n", c);
        if(x == kn + n - 1) throw 233;
        for(int i = 0; i < k; ++i)
        {
            int t = h * k + i;
            if(!vis[t])
            {
                vis[t] = true;
				c[x] = '0' + i;
                dfs(x + 1, t % (kn / k));
				c[x] = 0;
                vis[t] = false;
            }
        }
    }
    string crackSafe(int n, int k) {
        this->n = n; this->k = k;
        kn = 1;
        for(int i = 0; i < n; ++i) kn *= k;
        memset(vis, 0, sizeof(vis));
        memset(c, 0, sizeof(c));
        for(int i = 0; i < n - 1; ++i) c[i] = '0';
        try
        {
            dfs(n - 1, 0);
        }
        catch(int)
        {

        }
        return c;
    }
};

class Solution {
public:
    string crackSafe(int n, int k) {
        string result(n,'0'),s(n-1,'0');
        unordered_set<string> hash;
        hash.insert(result);
        while(1)
        {
            bool flag=true;
            for(int i=k-1;i>=0;i--)
            {
                char c=i+'0';
                if(hash.count(s+c)==0)
                {
                    hash.insert(s+c);
                    flag=false;
                    result+=c;
                    s+=c;
                    s.erase(s.begin());
                    break;
                }
            }
            if(flag==true)
                return result;
        }
    }
};

