#57
def prepare_line(line):
    lst = line.strip().split()
    l = len(lst)
    if l < 2:
        return "".join(lst)
    chcnt = sum(len(w) for w in lst)
    spneed= 80 - chcnt
    each , bals = divmod(spneed,l-1)
    multipliers = [each + 1] * bals + [each] * (l - bals - 1) + [0]
    return ''.join(w + ' ' * m for m, w in zip(multipliers, lst))    
    
    
import sys    
test_cases = open(sys.argv[1], 'r')
for tests in test_cases:
    balance = []
    new_lines = []
    tlen    = len(tests)
    while tlen > 80:
        line = tests[:80]
        bals = ''
        if tests[80] != ' ':
            line,bals = line.rsplit(" ", 1)
            done = 80 - len(bals)
        else:
            done = 81
        tests =  tests[done:]
        tlen  = tlen - done
        new_lines.append(prepare_line(line))
    tests = tests.strip()
    if tests:
        new_lines.append(tests)
    print "\n".join(new_lines)    
            
                
            
        
