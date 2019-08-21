import re
valids = re.compile(r'[a-h][1-8]-[a-h][1-8]')
for _ in range(int(input())):
    expr = input()
    if valids.match(expr) and len(expr)==5:
        row_from, col_from = expr[0], int(expr[1])
        row_to, col_to  = expr[3], int(expr[4])
        a = abs(ord(row_to) - ord(row_from))
        b = abs(col_to - col_from)        
        if a == 1 and b == 2 or a == 2 and b == 1:
            print("Yes")
        else:
            print("No")
        
    else:
        print("Error")
        