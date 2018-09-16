'''
Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and
there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
import operator
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def evals(a, b, op):
            if op == "+":return int(operator.add(a * 1.0, b))
            if op == "-":return int(operator.sub(a * 1.0, b))
            if op == "*":return int(operator.mul(a * 1.0, b))
            if op == "/":return int(operator.truediv(a * 1.0, b))


        stack = []
        for i in tokens:
            if  i in "+-*/" and len(stack)>=2:
                b, a = stack.pop(), stack.pop()
                stack.append(evals(a , b, i))
            else:
                stack.append(int(i))
            #print(stack)
        return stack[0]

print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))

