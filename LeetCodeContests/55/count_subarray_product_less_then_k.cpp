
class Solution {
    typedef vector<int> vi;
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int ans = 0;
        unordered_map<int, int> cnt;
        for(auto n:nums){
            unordered_map<int, int> tmp;
            for(auto p:cnt) if(p.first * n < k) {
                tmp[p.first * n] += p.second;
                ans += p.second;
            }
            if(n<k){
                tmp[n] += 1;
                ans += 1;
            }
            cnt.swap(tmp);
        }
        return ans;
    }
};

Solution sol = new Solution
prinf(sol.numSubarrayProductLessThanK([10, 5, 2, 6],100))