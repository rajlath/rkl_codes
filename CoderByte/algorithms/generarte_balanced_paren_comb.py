combinations = []
n = 0
def parens(left, right,strs=''):
    if not left and not right:
        combinations.append(strs)

    if left > 0:
        parens(left-1, right+1,strs+"(")


    if right > 0:
        parens(left, right-1, strs+")")



parens(3, 0)
print(*combinations)



