class Solution:
    def checkStraightLine(self, coordinates) :
        dx = coordinates[0][0] - coordinates[1][0]
        dy = coordinates[0][1] - coordinates[1][1]
        for i in range(2, len(coordinates)):
            x = coordinates[0][0] - coordinates[i][0]
            y = coordinates[0][1] - coordinates[i][1]
            if dx * y != dy * x:return False
        return True






'''
for (int i = 2; i < c.size(); i++) {
    long long dx = c[0][0] - c[1][0];
    long long dy = c[0][1] - c[1][1];
    long long ddx = c[0][0] - c[i][0];
    long long ddy = c[0][1] - c[i][1];
    if (dx * ddy != dy * ddx)return false;
}
    return true;
'''

print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))