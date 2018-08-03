'''
For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.
'''


crypt = ["A",
 "A",
 "A"]
solution = [["A","0"]]


def isCryptSolution(crypt, solution):
    solution = dict(solution)
    a, b, c = [convert_to_number(x, solution) for x in crypt]
    if not a or not b or not c: return False
    else:return int(a) + int(b) == int(c)


def convert_to_number(word, solution)    :
    ans = ''
    lens= len(word)
    for i, v in enumerate(word):
        ans += solution[v]
    if ans[0] == "0" and len(ans)>1: return False
    else: return ans



print(isCryptSolution(crypt, solution))
