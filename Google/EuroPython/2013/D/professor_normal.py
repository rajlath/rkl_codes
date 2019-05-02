import sys
from collections import defaultdict

def get_input_output_object():
    args = sys.argv
    if len(args) > 2:
        file_ins = open(sys.argv[1], "r")
        in_iter  = iter(file_ins.readlines())
        file_out = open(sys.argv[2], "w")
        return (in_iter, file_out)
    else:
        return (None, None)

ins, outs = get_input_output_object()
if ins != None:
    nb_test = int(next(ins))
    test_no = 1
    for t in range(nb_test):
        m = int(next(ins))
        n = int(next(ins))
        matrix = [[int(x) for x in next(ins).strip().split()] for _ in range(m)]
        exchanged = 0
        while True:
            matrix = [-1 if matrix[y][x] < 12 else matrix[y][x] for y in range(n) for x in range(m) ]
            print(matrix)
