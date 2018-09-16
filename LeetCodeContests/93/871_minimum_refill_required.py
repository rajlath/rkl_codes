'''
871. Minimum Number of Refueling Stops
User Accepted: 234
User Tried: 563
Total Accepted: 247
Total Submissions: 1546
Difficulty: Hard
A car travels from a starting position to a destination which is target miles east of the starting position.
Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east
of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.
It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
What is the least number of refueling stops the car must make in order to reach its destination?
If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation:
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.


Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

#solution by https://leetcode.com/yangzhenjian
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        stations.append([target, 0])
        n = len(stations)
        MINF = - 10 ** 15

        dp = [startFuel] + [MINF] * n
        px = 0
        for i, (x, f) in enumerate(stations, 1):
            dp_next = [MINF] * (n + 1)
            for j in range(i + 1):
                if dp[j] >= x - px:
                    dp_next[j] = dp[j] - (x - px)
                if j > 0 and dp[j-1] >= x - px:
                    dp_next[j] = max(dp_next[j], dp[j-1] - (x - px) + f)
            px = x
            dp = dp_next
        for j in range(n):
            if dp[j] >= 0:
                return j
        return -1

# cpp solutin by https://leetcode.com/shdut

#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <ctime>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <assert.h>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define x first
#define y second
#define all(x) x.begin(),x.end()
#define pb push_back
#define mp make_pair
#define SZ(x) int(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define pi acos(-1)
#define mod 998244353 //1000000007
#define inf 1000000007
#define ll long long
#define DBG(x) cerr<<(#x)<<"="<<x<<"\n";
#define N 100010

template <class U,class T> void Max(U &x, T y){if(x<y)x=y;}
template <class U,class T> void Min(U &x, T y){if(x>y)x=y;}
template <class T> void add(int &a,T b){a=(a+b)%mod;}

int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=1LL*ans*a%mod;
        a=1LL*a*a%mod;b>>=1;
    }
    return ans;
}

pii a[510];
ll dp[510][510];
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
		int sz=0;
		a[sz++]={0,startFuel};
		for(auto &o:stations)a[sz++]={o[0],o[1]};
		a[sz++]={target,0};
		rep(i,0,sz)rep(j,0,i+1)dp[i][j]=-1;
		dp[0][0]=0;
		rep(i,0,sz-1){
			rep(j,0,i+1){
				if(dp[i][j]>=0){
					ll w=dp[i][j]-(a[i+1].x-a[i].x);
					if(w>=0)Max(dp[i+1][j],w);
					w+=a[i].y;
					if(w>=0)Max(dp[i+1][j+1],w);
				}
			}
		}
		rep(i,0,sz)if(dp[sz-1][i]>=0)return i-1;
		return -1;
    }
};
'''
# my version of https://leetcode.com/shdut solution in cpp
# TLE solution
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        size = 0
        a = []
        a.append((0, startFuel))
        for x in stations:a.append((x[0],x[1]))
        a.append((target, 0))
        size = len(a)
        dp = [[-1 for x in range(size+1)] for y in range(size+1)]
        dp[0][0] = 0
        for i in range(size-1):
            for j in range(i+1):
                if dp[i][j] >= 0:
                    w = dp[i][j] - (a[i+1][0] - a[i][0])
                    if w >= 0:dp[i+1][j] = max(dp[i+1][j], w)
                    w += a[i][1]
                    if w >= 0:dp[i+1][j+1] = max(dp[i+1][j+1],w)
        for i in range(size):
            if dp[size-1][i] >=0:return i-1
        return -1

#awice solution
#
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1

class Solution(object):
    def refuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans








print(Solution().minRefuelStops(1, 1, []))


