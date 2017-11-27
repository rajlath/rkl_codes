class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves = [x for x in moves]
        if len(moves)==1:return("false")
        else:
            if moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D"):
                return("YES")
            else:
                return("NO")
                
sol = Solution()
print(sol.judgeCircle("LL"))                
        
