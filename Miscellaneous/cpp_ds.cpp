#include <bits/stdc++.h>
using namespace std;

int print_array(vector<int> v)
{
    for (auto x : v)
    {
        cout<<x<<"\n";
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    /*
    string a = "rajlath";
    string b = a + a;
    cout<<b<<"\n";
    cout<<b[5]<<"\n";
    b[5] = 'x';
    cout<<b<<"\n";
    string c = b.substr(3, 4);
    cout<<c<<"\n";
    int i = b.find("z");
    if (i > b.size()){ cout<<"Not found."<<"\n"; }
    else{ cout << i <<"\n"; }
    */
    set <int> st ;
    st.insert(5);
    st.insert(12);
    st.insert(70);
    st.insert(72);
    /*
    cout << st.size() << "\n";
    cout << st.count(5) << "\n";
    cout << st.count(123) << "\n";
    auto it = st.begin();
    for (auto it = st.begin(); it != st.end(); it++)
    {
        cout<<*it<<"\n";
    }

    auto it1 = st.find(14);
    auto it2 = st.begin();
    if (it1 == st.end()){ cout<<"Not found."<< "\n"; }

    cout<<*it1<<"\n";
    */
    priority_queue<int> pq;
    pq.push(4);
    pq.push(5);
    pq.push(2);
    pq.push(56);
    cout << pq.top()<<"\n";
    pq.pop();
    cout << pq.top()<<"\n";
    pq.pop();
    cout << pq.top()<<"\n";

    priority_queue<int,vector<int>,greater<int>> q;









}
