#include <cmath>
#include <cstdio>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
#define ll long long
#define MAX 200005
ll SEG[4*MAX];
ll arr[MAX];
ll mapped[MAX];
pair<ll,pair<ll,ll>> hi[MAX];

void update(int node, int start, int end, int idx, ll val){
    if(start==end){
        SEG[node]=val;
    }
    else{
        ll mid=(start+end)>>1;
        if(idx>mid) update(2*node+1, mid+1, end, idx, val);
        else update(2*node, start, mid, idx, val);
        SEG[node]=max(SEG[2*node], SEG[2*node+1]);
    }
}

ll query(int node, int start, int end, int l, int r){
    if(start>end || l>r || l>end || r<start) return -1;
    if(start>=l && end<=r){
        return SEG[node];
    }
    int mid=(start+end)>>1;
    return max(query(2*node, start, mid, l, r), query(2*node+1, mid+1, end, l, r));
}


map<ll,int> MM;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>> hi[i].first >> hi[i].second.first;
        hi[i].second.second=i;

    }
    sort(hi, hi+n);
    for(int i=0; i<n; i++){
        mapped[hi[i].second.second]=i;
        MM[hi[i].first]=i;
    }
    for(int i=0; i<n; i++){
        update(1, 0, n-1, i, hi[i].second.first);
    }
    int q;cin>>q;
    while(q--){
        char s;cin>>s;ll idx;cin>>idx;

        if(s=='d'){

            idx=MM[idx];
            update(1,0,n-1,idx,-1);
        }
        else{
            idx--;
            idx=mapped[idx];
            ll vall=query(1,0,n-1,idx,idx);
            if(vall==-1){
                cout << "DROWNED" << endl;
                continue;
            }
            int start=idx+1;
            int end=n-1;
            while(start<=end){
                int mid=(start+end)>>1;
                if(query(1,0,n-1,start,mid)>vall) end=mid-1;
                else start=mid+1;
            }
            if(start==n){
                cout << "IMPOSSIBLE" << endl;
            }
            else{
                cout << hi[start].first << endl;
            }
        }
    }
    return 0;
}