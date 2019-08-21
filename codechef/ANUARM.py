for _ in range(int(input())):
    nb_op, nb = [int(x) for x in input().split()]
    lines = sorted([int(x) for x in input().split()])
    result = [0] * nb_op
    for i in range(nb_op):
        p = abs(lines[0] - i)
        q = abs(lines[-1] - i)
        result[i] = max(p, q)
    print(*result)    
        
    