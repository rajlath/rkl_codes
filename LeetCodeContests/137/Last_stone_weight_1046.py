class Solution:
  def lastStoneWeight(self, stones):
    while len(stones) > 1:
      x, y = stones.pop(stones.index(max(stones))), stones.pop(stones.index(max(stones)))
      if x == y:
        if len(stones) == 0:
          return 0
      else:
        stones.append(max(x, y) - min(x, y))
    if stones:
      return stones[0]
    else:
      return 0

print(Solution().lastStoneWeight([10,4,2,10]))
