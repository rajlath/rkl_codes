nb, need = [int(x) for x in input().split()]
elems = sorted([(int(v), i+1) for i, v in enumerate(input().split())])
answer = "IMPOSSIBLE"
left, rite = 0, nb - 1
while rite > left:
    k = elems[left][0] +  elems[rite][0]
    if k == need:
        answer = str(elems[left][1]) +" " + str(elems[rite][1])
        break
    if k < need: left +=1
    else: rite -= 1
print(answer)




