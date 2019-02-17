from collections import namedtuple, defaultdict

def get_lines():
    lines = []
    with open("input.txt") as f:
        for line in f:
            lines.append(line)
    return lines

lines = get_lines()

Program = namedtuple("Program", ["name", "weight", "leaves"])

def build_tree():
    for line in lines:
        name = ''
        for i in lines:
            if i != ' ':
                name += i
            else:
                break
        print(name)
build_tree

