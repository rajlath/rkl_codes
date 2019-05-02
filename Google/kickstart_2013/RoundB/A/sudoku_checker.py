import sys
def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line.strip() for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return (None, None)


def is_valid_row(row):
    need = set([1,2,3,4,5,6,7,8,9])
    return set(row).intersection(need) == need

inputs , outs = get_input_output()

indx = 0
test = 1

if inputs != None:
    nb_test = int(inputs[indx])
    #print(nb_test, indx)
    indx += 1
    for _ in range(nb_test):
        n = int(inputs[indx])
        indx += 1
        sudoku = []
        for i in range(n * n):
            sudoku.append([int(x) for x in inputs[indx].strip().split()])
            indx += 1
        flag = True
        for i in range(n * n):
            if not is_valid_row(sudoku[i]):
                flag = False
                break
        if flag:
            sudocol = list(zip(*sudoku))
            for i in range(n * n):
                if not is_valid_row(sudocol[i]):
                    flag = False
                    break
        if flag:
            for i in range(n):
                for j in range(n):
                    v = []
                    for x in range(n):
                        for y in range(n):
                            v.append(sudoku[i * n + x][j * n + y])
                    if not is_valid_row(v):
                        flag = False
        ans = ["No", "Yes"][flag == True]
        ans1 = "Case #{}: {}".format(test, ans)
        test += 1
        print(ans1, file = outs)

