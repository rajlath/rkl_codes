notation = "2kr3r/pp1nbppp/3p1n2/q1pPp1B1/4P1b1/2N2N2/PPP1BPPP/R2Q2RK"
# comments

def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def build_normal_board(rotated):
    normal_board = []
    for i in rotated:
        curr = ''
        pos = 0
        x = 0
        while pos < len(i):
            if i[pos] == ' ':
                x += 1
                pos += 1
            else:
                if x != 0:
                    curr += str(x)
                    x = 0
                curr += i[pos]
                pos += 1
        if x != 0:curr += str(x)

        normal_board.append(curr)
    return normal_board





def chessNotation(notation):
    board = [x for x in notation.split("/")]
    normal_board = []
    for i in board:
        curr = []
        for j in i:
            if j.isdigit():
                for i in range(int(j)):
                    curr.append(" ")
            else:
                curr.append(j)
        normal_board.append(curr)

    # rotate board by 90 degree clockwise
    rboard =  rotate90Clockwise(normal_board)
    return "/".join(build_normal_board(rboard))

print(chessNotation(notation))

'''
Input:
notation: "2kr3r/pp1nbppp/3p1n2/q1pPp1B1/4P1b1/2N2N2/PPP1BPPP/R2Q2RK"
Output:
"RP2q1p/1P4p/1PN1p2k/Q3Ppnr/1B1Pp1b/1PN2np/RP1bB1p/KP4pr"
"RP2q1p1/1P4p1/1PN1p2k/Q3Ppnr/1B1Pp1b1/1PN2np1/RP1bB1p1/KP4pr"
"RP2q1p1/1P4p1/1PN1p2k/Q3Ppnr/1B1Pp1b1/1PN2np1/RP1bB1p1/KP4pr
'''
def expand(notation):
    for i in range(1,9):
        notation = notation.replace(str(i),'1'*i)
    return notation

def contract(notation):
    for i in list(range(1,9))[::-1]:
        notation = notation.replace('1'*i,str(i))
    return notation

def transpose(ls):
    return [''.join(ls[i][j] for i in range(len(ls)))[::-1] for j in range(len(ls[0]))]

def chessNotation(notation):
    return contract('/'.join(transpose(expand(notation).split('/'))))





