class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: : List[List[int]]
        :rtype: :  -> int
        """
        lens = len(books)
        dp = [0] + [int(10 ** 18)] * lens
        for i in range(lens):
            width = 0
            height= 0
            for j in range(i, lens):
                width += books[j][0]
                height = max(height, books[j][1])
                if width <= shelf_width:
                       dp[j + 1] = min(dp[j + 1], dp[i] + height)

        return dp[lens]
print(Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))