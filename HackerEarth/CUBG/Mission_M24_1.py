def rotate(matrix):
    a=[]
    for j in range(len(matrix[0])):
        a.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])-1,-1,-1):
            a[len(matrix[0])-1-j].append(matrix[i][j])
    return a

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    b=[]
    if matrix==[]:
        return []
    while True:
        b+=matrix[0]
        del matrix[0]
        if matrix!=[]:
            matrix=rotate(matrix)
        else:
            break
    return b

n = int(input())
l, inc, health = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append([x for x in input().split()])

flattend = spiralOrder(matrix)
for i in flattend:
    if i == "O":
        health -= l
    elif i == "+"    :
        health += inc
    if health == 0:break
if health == 0:
    print("NO")
else:
    print("YES")