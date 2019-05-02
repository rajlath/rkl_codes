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
        nb_pairs = int(next(ins))
        players = [ [x for x in  next(ins).strip().split()] for _ in range(nb_pairs)]
        ok = "NO"
        p1, p2 = players.pop()
        A = {p1}
        B = {p2}
        while players:
            players, current = [], players
            for p1, p2 in current:
                if p1 in A:
                    if p2 not in A:
                        B.add(p2)
                    else:
                        break
                elif p1 in B:
                    if p2 not in B:
                        A.add(p2)
                    else:
                        break
                elif p2 in A:
                    if p1 not in A:
                        B.add(p1)
                    else:
                        break
                elif p2 in B:
                    if p1 not in B:
                        A.add(p1)
                    else:
                        break
                else:
                    players.append((p1, p2))
            else:
                continue
            break
        else:
            ok = 'Yes'

        ans1 = 'Case #{}: {}'.format(t + 1, ok)
        print(ans1, file = outs)
else:
    print("Invalid IO")



