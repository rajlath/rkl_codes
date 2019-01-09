
def solve(arrA, lens):
    if    lens <= 1:    return  0
    elif  arrA[0] == 0: return -1
    else:
        canJumpTo = arrA[0]
        step      = arrA[0]
        jump      = 1
        for i in range(1, lens):
            if i == lens - 1:
                return jump
            canJumpTo = max(canJumpTo, i + arrA[i])
            step -= 1
            if step == 0: jump +=1
            if i >= canJumpTo:
                return -1
            step = canJumpTo - i
    return -1

nb_Test = int(input())
for _ in range(nb_Test):
    lens =  int(input())
    arrA =  [int(x) for x in input().split()]
    print(solve(arrA, lens))






