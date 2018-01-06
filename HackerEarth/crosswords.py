x = [ -1, -1, -1, 0, 0, 1, 1, 1]
y = [ -1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())

def searchMat(crossword, row, col, word):

    if(crossword[row][col] != word[0]):
        return False

    l = len(word)

    for d in range(8):
        rd = row + x[d]
        cd = col + y[d]
        k = 0
        for k in range(1, l):
            if( rd >= n or rd < 0 or cd >= n or cd < 0):
                break

            if( crossword[rd][cd] != word[k]):
                break

            rd += x[d]
            cd += y[d]

        if (k+1) == l:
            return True

    return False

crossroad = []
for i in range(n):
    s = input()
    crossroad.append(s.split(" "))

w = int(input())
count = 0
for i in range(w):
    temp = False
    word = input()
    for i in range(n):
        for j in range(n):
            if searchMat(crossroad, i, j, word):
                temp = True
    if temp:
        count += 1

if w == count:
    print("True")
else:
    print("False")