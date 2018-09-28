class Solution:
def totalFruit(self, tree):
    b0, b1, p0, p1 = [-1] * 4
    ret, la = 0, 0
    for i, t in enumerate(tree):
        if t == b0:
            p0 = i
        elif t == b1:
            p1 = i
        else:
            if p1 < p0:
                b0, p0, b1, p1 = b1, p1, b0, p0
            b0, p0, la = t, i, p0+1
        ret = max(ret, i-la+1)
    return ret

const int N = 1e5 + 7;
int cnt[N];

class Solution {
public:
    int totalFruit(vector<int>& t) {
        rep(i, 0, sz(t)) cnt[t[i]] = 0;
        int type = 0, ret = 0;
        for (int l = 0, r = 0; r < sz(t); ++r) {
            if (++cnt[t[r]] == 1) ++type;
            while (type > 2) {
                if (--cnt[t[l++]] == 0) --type;
            }
            ret = max(ret, r - l + 1);
        }
        return ret;
    }
};

int cnt[40001];
class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int n=tree.size();
    for(int i=0;i<n;i++)
    {
        cnt[i]=0;
    }
    int ans=0;
    int l=0,r=0,kind=0;
    while(r<n)
    {
        while(r<n&&kind<3)
        {
            cnt[tree[r]]++;
            if(cnt[tree[r]]==1)kind++;
            r++;
            if(kind<3)ans=max(ans,r-l);
        }
        while(l<r&&kind==3)
        {
            cnt[tree[l]]--;
            if(cnt[tree[l]]==0)kind--;
            l++;
            if(kind<3)ans=max(ans,r-l);
        }
    }
    return ans;
    }
};

const ll MOD=1e9+7;
class Solution {
public:
int totalFruit(vector<int>& tree) {
    int N=tree.size();
    if(N==0) return 0;
    int cur=-1,prv=-1,cnt1=0,cnt2=0;
    int res=0;
    for(int k:tree){
    if(k==cur){
        cnt1++,cnt2++;
    }else if(k==prv){
        swap(cur,prv);
        cnt1=1;
        cnt2++;
    }else{
        cnt2=cnt1+1;
        cnt1=1;
        prv=cur;
        cur=k;
    }
    res=max(res,cnt2);
    }
    return res;
}
};
