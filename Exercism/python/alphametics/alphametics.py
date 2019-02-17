from itertools import combinations, permutations

def calc(wrd, dicts):
    return sum(dicts[b] * 10 ** (len(wrd) - i - 1) for i, b in enumerate(wrd))
def solve(puzzle):
    '''get all the words'''
    equation , result = puzzle.split("==")
    result = result.strip()
    operands = [x.strip() for x in equation.split("+")]
    '''find all the unique chars used in the puzzle'''
    chars = set([x for lst in operands + [result] for x in lst])
    can_not_be_zero = set(n[0] for n in operands + [result])
    #print(can_not_be_zero)

    for number in combinations(range(10), len(chars)):
        for ch in permutations(chars):
            candidate = {ch[i]:n for i, n in enumerate(number)}
            if any(candidate[n] == 0 for n in can_not_be_zero):continue
            equ_sum = sum([calc(cur, candidate) for cur in operands])
            result_val = calc(result, candidate)
            if result_val == equ_sum:
                return candidate

    return {}



print(solve("A == B"))