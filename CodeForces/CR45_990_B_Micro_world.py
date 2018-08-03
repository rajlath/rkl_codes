'''
Examples
inputCopy
7 1
101 53 42 102 101 55 54
outputCopy
3
inputCopy
6 5
20 15 10 15 20 25
outputCopy
1
inputCopy
7 1000000
1 1 1 1 1 1 1
outputCopy
7
'''

n, k = [int(x) for x in input().split()]
bact = [int(x) for x in input().split()]
sb = bact[:]
stack = [sb[0]]
print(sb, stack)
while True:
    for i in range(1, len(sb)):
        if sb[i] - sb[i-1] <= k and  sb[i] - sb[i-1] > 0 :
            continue
        else:
            stack.append(sb[i])
            print(stack)
    if len(stack) == len(sb):
        break
    else:
        sb = stack[:]
        stack.clear()
        print(sb)
print(len(sb))









