'''
sample input
sample output
Hi:) (it is me) I have bad news:-((
3

sample input
sample output
((two plus two equals four))
2
'''
s = input()
stack = []
cnt = 0
for i in s:
    if i in "()":
        if len(stack) > 0:
            if i == "(" and stack[-1] == ")":
                stack.pop()
                continue
            else:
                cnt += 2
                stack.pop()



    else:
        continue
