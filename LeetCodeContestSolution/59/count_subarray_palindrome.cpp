/*
 * Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.
 * A subsequence of a string S is obtained by deleting 0 or more characters from S.
 * A sequence is palindromic if it is equal to the sequence reversed.
 * Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
 * 
 * Example 1:
 * Input:
 * S = 'bccb'
 * Output: 6
 * Explanation:
 * The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
 * Note that 'bcb' is counted only once, even though it occurs twice.
 * 
 * Example 2:
 * Input:
 * S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
 * Output: 104860361
 * Explanation:
 * There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
 * 
 * 
 * Note:
 * The length of S will be in the range [1, 1000].
 * Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
 * Solution
 * Python constantly failed even if implementation is exactly as coded 
 * here in cpp.. So this cpp solution.
 * You have to understand from code 
*/
const int mod = 1000000007;
typedef vector<int> vi;
int dp[1001][1001];

class Solution {
    map<char, vi> prev, next;
    int cntP(int l, int r){
        if(l>r) return 0;
        if(dp[l][r] >= 0) return dp[l][r];
        dp[l][r] = 0;
        for(int c = 'a';c<='d';++c) if(next[c][l]<=r){
            int l1 = next[c][l];
            int r1 = prev[c][r];
            dp[l][r] += cntP(l1+1, r1-1) + 1;
            if(l1<r1) dp[l][r] += 1;
            dp[l][r] %= mod;
        }
        return dp[l][r];
    }
public:
    int countPalindromicSubsequences(string S) {
        map<char, int> pos;
        int n = S.size();
        for(char c='a';c<='d';++c) {
        	prev[c] = vi(n,-1);
        	next[c] = vi(n, n);
		}
        pos['a'] = pos['b'] = pos['c'] = pos['d'] = -1;
        for(int i=0;i<n;++i){
            pos[S[i]] = i;
            for(char c='a';c<='d';++c) prev[c][i] = pos[c];
        }
        pos['a'] = pos['b'] = pos['c'] = pos['d'] = n;
        for(int i=n-1;i>=0;--i){
            pos[S[i]] = i;
            for(char c='a';c<='d';++c) next[c][i] = pos[c];
        }
        pos['a'] = pos['b'] = pos['c'] = pos['d'] = 0;
        memset(dp, -1, sizeof(dp));
        return cntP(0, n-1);
    }
};
