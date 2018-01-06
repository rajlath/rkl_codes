'''
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.

solution : 
sol1: we iterate through left and right+1 -because right is also included
      subject each element to a helper function
      helper function:This function takes an integer.Convert this number
      to an array of digits..Iterate over this array and check if every
      element can divide the main number..if it fails at any check it
      return false and if iteration is completed it return true
      all the true returns are collected in a list
      this list is printed as answer..
sol2: we use list comprehension for checking and adding valid number in 
      a list      
      
'''

class Solution(object):
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def good(num):
            nList = map(int, str(num))
            for i in nList:
                if i == 0:
                    return False
                if num%i != 0:
                    return False
            return True
        ans = []
        for i in range(left, right+1):
            if good(i):
                ans.append(i)
        return ans
        
    
    def is_self_divider(self,n):
            """
            :type n int
            :rtype boolean
            """
            st = [int(x) for x in str(n) if x != "0"]
            cnt = sum([1 for  x in st if n%x == 0])
            return cnt == len(str(n))
            
    def selfDividingNumbers1(self,left,right):
            """
            :type left : int
            :type right: int
            :rtype : List(int)
            """
            outs = [x for x in range(left,right+1) if self.is_self_divider(x)]
            return outs
sol = Solution()
print(sol.selfDividingNumbers(1,22))
print(sol.selfDividingNumbers1(1,22))       
             
          
