


class Solution:

    def basic_calculator_III(self,expr):
        l1, l2, o1, o2 = 0, 1, 1, 1
        digs = ["1","2","3","4","5","6","7","8","9","0"]
        i = 0
        while i < len(expr):
            curr = expr[i]
            if curr in digs:
                nums = curr
                while i+1 < len(expr) and expr[i+1] in digs:
                    nums += expr[i+1]
                    i+= 1
                num = int(nums)
                l2 = [l2 // [num,1][num==0]  , l2 * num][o2 == 1]
            elif curr == "(":
                j   = i
                cnt = 0
                while i < len(expr):
                    cnt += expr[i] == "("
                    cnt -= expr[i] == ")"
                    if cnt == 0:
                        break
                    i+=1
                num = self.basic_calculator_III(expr[j+1:i])
                l2 = [l2 // [num,1][num==0], l2 * num][o2 == 1]

            elif curr in ["*", "/"]:
                o2 = [-1, 1][curr == '*']

            elif curr in ['+' ,'-']:
                l1 = l1 + o1 * l2
                o1 = [-1, 1][curr == '+']
                l2 = 1
                o2 = 1
            i+=1
        return (l1 + o1 * l2)


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self. basic_calculator_III(s)


sol = Solution()
print(sol.calculate("(7)-(0)+(4)"))



