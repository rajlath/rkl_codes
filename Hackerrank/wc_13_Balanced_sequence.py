'''
Sample Input 0

8
(((()(((
Sample Output 0

1
'''
input()
s = input()

stack = []
for c in s:
    if len(stack) == 0 or stack[-1] + c != "()": stack.append(c)
    else:stack.pop()
    print(stack)
print(min(stack.count(")"), 1) + min(stack.count("("), 1) )