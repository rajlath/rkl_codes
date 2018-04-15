'''
Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]class Solution {
private:
    void helper(string S, int idx, vector<string> &res) {
        if (idx == S.size()) {
            res.push_back(S);
            return;
        }
        if (isalpha(S[idx])) {
            S[idx] = tolower(S[idx]);
            helper(S, idx + 1, res);
            S[idx] = toupper(S[idx]);
            helper(S, idx + 1, res);
        } else {
            helper(S, idx + 1, res);
        }
    }

public:
    vector<string> letterCasePermutation(string S) {
        vector<string> res;
        helper(S, 0, res);
        return res;
    }
};
'''



from string import ascii_letters as le
class Solution(object):
    ans = []
    def helper(self,s, indx, res):
        global ans
        if indx == len(s):
            self.ans.append(res)
            return self.ans
        elif s[indx] in le:
            self.helper(s, indx+1, res+[s[indx].lower()])
            self.helper(s, indx+1, res+[s[indx].upper()])
        else:
            self.helper(s, indx+1, res+[s[indx]])






    def letterCasePermutation(self, S):
        """
        :type S: str
        :rty
        """
        res = []
        self.helper(list(S),0, res)
        return res

sol = Solution()
print(sol.letterCasePermutation("a1b2"))

