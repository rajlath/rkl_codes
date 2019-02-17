import operator
from collections import defaultdict

def get_lines():
    lines = []
    filename = r"E:\rkl_codes\AdventOfCodes\2017\day_8\input.txt"
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    return lines
instructions = {
                'inc': operator.add,
                'dec': operator.sub
                }

comparators = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne
}

def parse_instruction(line):
    tokens = line.split()
    return (tokens[0], instructions[tokens[1]],int(tokens[2]),
            tokens[4], comparators[tokens[5]] ,int(tokens[6])
           )

def run_instructions(command):
    register = defaultdict(int)
    max_at_runs = 0
    for i in command:
        reg, op, val, cmp_reg, cmp_op, cmp_val = i
        if cmp_op(register[cmp_reg], cmp_val):
            register[reg] = op(register[reg], val)
        max_at_runs = max(register.values())
    max_at_end = max(register.values())
    return (max_at_end, max_at_runs)




if __name__ == '__main__'    :
    lines = get_lines()
    command = [parse_instruction(i) for i in lines]
    max_at_end, max_at_runs = run_instructions(command)
    print("At end {} and over all {}".format(max_at_end, max_at_runs))



