'''
input
5
weird
output
werd
input
4
word
output
word
input
5
aaeaa
output
a
'''
nol = int(input())
ans = []
ins = input()
for i in ins:
    if len(ans)> 0 and ans[-1] in "aeiouy" and i in "aeiouy":continue
    else:
        ans.append(i)
print("".join(ans))


