class Solution:
  def removeDuplicates(self, S):
    valids = []
    for i in S:
      if len(valids) > 0:
        if valids[-1] == i:
          valids.pop()
          continue
      valids.append(i)

    return "".join(valids)

print(Solution().removeDuplicates("abbaca"))














