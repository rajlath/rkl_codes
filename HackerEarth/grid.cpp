// Grid

#include <bits/stdc++.h>
using namespace std;

int visit[1003][1003], level[1003][1003];

string S[1003];
queue< pair<int, int> > Q;

int main()
{
cin.tie(NULL), cout.tie(NULL);

int N, M, q;
cin >> N >> M >> q;

for(int i=0; i<N; i++)
cin >> S[i];

int x, y;
cin >> x >> y;

memset(level, -1, sizeof(level));

int lvl = 0;
Q.push(make_pair(x-1, y-1));

while(!Q.empty())
{
int q = Q.size();

while(q--)
{
pair<int, int> x = Q.front();
Q.pop();
int a = x.first, b = x.second;

if(a < 0 || b < 0 || a >= N || b >= M || visit[a][b] || S[a][b] == '*')
continue;

visit[a][b] = 1;
level[a][b] = lvl;

Q.push(make_pair(a-1, b));
Q.push(make_pair(a+1, b));
Q.push(make_pair(a, b-1));
Q.push(make_pair(a, b+1));
}

lvl++;
}

while(q--)
{
int x, y;
cin >> x >> y;

cout << level[x-1][y-1] << "\n";
}

return 0;
}