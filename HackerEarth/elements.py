'''
2
4 7
ZS mm Lv Fz Yo Hq Nd
VX Md cc lR oB gO Ng
rz lb ng la Hk XK qe
NH EW RF qS Ki QA yF
Hk
3 1
q
h
S
M
'''
for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    matrix = []
    found = False
    for i in range(m):
        matrix.append([x for x in input().split()])
    target = input()
    ans = ""
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for j in range(left, right + 1):
            curr = matrix[top][j]
            if curr == target:
                found = True
                break
            else:ans +=curr
        if found:break
        for i in range(top + 1, bottom):
            curr = matrix[i][right]
            if curr == target:
                found = True
                break
            else:ans += curr
        if found:break
        for j in reversed(range(left, right + 1)):
            if top < bottom:
                curr = matrix[bottom][j]
                if curr == target:
                    found = True
                    break
                else:ans += curr
        if found:break
        for i in reversed(range(top + 1, bottom)):
                if left < right:
                    curr = matrix[i][left]
                    if curr == target:
                        found = True
                        break
                    else: ans += curr
        if found:break
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    if found:print(ans+target)
    else:print("NO")



