/*
741. Cherry Pickup My SubmissionsBack to Contest

Difficulty: Hard
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells
(cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
*/
#include<iostream>
using namespace std;
#include <bits/stdc++.h>
class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        dp[0][0] = grid[0][0];
        for (int i = 1; i < 2 * n - 1; i++) {
            vector<vector<int>> curr(n, vector<int>(n, -1));
            for (int j = 0; j < n && j <= i; j++) {
                for (int k = 0; k < n && k <= i; k++) {
                    if (grid[j][i - j] < 0 || grid[k][i - k] < 0) continue;
                    int t = dp[j][k];
                    if (j > 0) t = max(t, dp[j - 1][k]);
                    if (k > 0) t = max(t, dp[j][k - 1]);
                    if (j > 0 && k > 0) t = max(t, dp[j - 1][k - 1]);
                    if (t < 0) continue;
                    t += j == k ? grid[j][i - j] : grid[j][i - j] + grid[k][i - k];
                    curr[j][k] = t;
                }
            }
            dp = curr;
        }
        return max(dp[n - 1][n - 1], 0);
    }
};