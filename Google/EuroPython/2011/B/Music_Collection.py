import sys
from collections import defaultdict

def get_answer(songs):
    if len(songs) == 1: return [""]
    subs = defaultdict(int)
    for name in songs:
        lens = len(name)
        name_l = name.lower()
        done = set()
        for i in range(lens - 1):
            for j in range(i + 1, lens):
                curr = name_l[i:j]
                if curr in done:continue
                else:
                    done.add(curr)
                    subs[curr] += 1
    res = [k for k, v in subs.items() if v == 1]
    res.sort(key = lambda s: len(s))

    out = []
    for name in songs:
        matched = []
        name_lc = name.lower()
        for s in res:
            if s in name_lc:
                matched.append(s)
        if matched:
            min_len = len(matched[0])
            xxx = [x for x in matched if len(x) == min_len]
            item = sorted(xxx)[0].upper()
            out.append(item)
        else:
            out.append(None)
    return out

def get_input_output_obj():
    args = sys.argv
    if len(args) >= 2:
        ins = open(args[1], "r")
        out = open(args[2], "w")
        return (ins, out)
    else:
        return (None, None)

def read_line(ins):
    return ins.readline().strip()

in_file, out_file = get_input_output_obj()
if in_file is not None:
    tests = 1
    nb_test = int(read_line(in_file))
    for _ in range(nb_test):
        songs = []
        nb_songs = int(read_line(in_file))
        for _ in range(nb_songs):
            songs.append(read_line(in_file))

        line = "Case #{}: ".format(tests)
        print(line, file = out_file)
        tests += 1

        res = get_answer(songs)
        for s in res:
            ans = '"' + s +'"' if s is not None else ":("
            print(ans, file = out_file)



else:
    print("Invalid input or output file.")