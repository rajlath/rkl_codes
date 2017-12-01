/*
715. Range Module My SubmissionsBack to Contest
User Accepted: 61
User Tried: 171
Total Accepted: 61
Total Submissions: 387
Difficulty: Hard
A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.
removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).
Example 1:
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
Note:

A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
*/
typedef pair<int, int> ii;
class RangeModule {
    set<ii> Is;
public:
    RangeModule() {
        Is.insert(ii(-1,0));
        Is.insert(ii(1E9,1E9+1));
    }

    void addRange(int left, int right) {
        auto it = --Is.upper_bound(ii(left,0));
        if(it->second < left){
            ++it;
        }
        else{
            left = it->first;
        }
        while(it!=Is.end() && it->first<=right){
            right = max(right, it->second);
            it = Is.erase(it);
        }
        Is.insert(ii(left, right));

    }

    bool queryRange(int left, int right) {
        auto it = --Is.upper_bound(ii(left,1E9));
        return it->second >= right;
    }

    void removeRange(int left, int right) {
        auto it = --Is.upper_bound(ii(left,0));
        if(it->second <= left) it++;
        else{
            int l = it->first, r = left;
            Is.insert(ii(l,r));
        }
        while(it!=Is.end() && it->second <= right){
            it = Is.erase(it);
        }
        if(it->first < right){
            int l = right, r = it->second;
            it = Is.erase(it);
            Is.insert(ii(l,r));
        }

    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * bool param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */