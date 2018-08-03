from string import ascii_uppercase as uc
prefix = input().strip()
s = uc
p = prefix[::-1]
stack = []

for i in p:
    if i in s:
        stack.append(i)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b + i)
print(*stack)