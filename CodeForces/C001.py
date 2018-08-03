nops = int(input())
stacks= [""]
for i in range(nops):
    op = [x for x in input().split()]
    if op[0] is "1":
        cur = stacks[-1] + op[1]
        stacks.append(cur)
        #print(stacks)
    elif op[0] is "2":
        last = stacks[-1]
        #print(last)
        cnt  = int(op[1])
        cur  = last[:len(last)-cnt]
        stacks.append(cur)
        #print(stacks)
    elif op[0] is "3":
        last = stacks[-1]
        cnt  = int(op[1])
        print(last[cnt-1])
    else:
        stacks.pop(-1)
        #print(stacks)







